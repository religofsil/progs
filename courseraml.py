def strt(num):
    print '---------------'+str(num)+' - start---------------'
def nnd(num):
    print '----------------'+str(num)+' - end----------------\n'
def assg_send(assignment, num, data):
    import codecs
    f=codecs.open('courseraml-'+str(assignment)+'.'+str(num)+'.txt', 'w', 'utf-8')
    f.write(data)
    f.close()
def rndr(data):
    import numpy as np
    return np.around(data, decimals=2)
    
def assignment0():
    import numpy as np
    #1
    strt(1)
    X=np.random.normal(loc=1, scale=10, size=(1000, 50))
    print X
    nnd(1)
    #2
    strt(2)
    mean=np.mean(X, axis=0)
    std=np.std(X, axis=0)
    X=(X-mean)/std
    print X
    nnd(2)
    #3
    strt(3)
    Z = np.array([[4, 5, 0], 
             [1, 9, 3],              
             [5, 1, 1],
             [3, 3, 3], 
             [9, 9, 9], 
             [4, 7, 1]])
    sums=np.sum(Z, axis=1)
    print sums
    print np.nonzero(sums>10)
    nnd(3)
    #4
    strt(4)
    lefteye=np.eye(3)
    righteye=np.eye(3)
    eyes=np.vstack((lefteye, righteye))
    print eyes
    nnd(4)
    
def assignment1():
    import numpy as np
    import pandas
    data = pandas.read_csv('titanic.csv', index_col='PassengerId')
    print data.head()
    #1
    strt(1)
    male=np.sum(data['Sex']=='male')
    female=np.sum(data['Sex']=='female')
    assg_send(1, 1, str(male)+' '+str(female))
    nnd(1)
    #2
    strt(2)
    survivors=np.sum(data['Survived'])
    #print survivors
    percentage=(float(survivors)/891)*100
    assg_send(1, 2, str(rndr(percentage)))
    nnd(2)
    #3
    strt(3)
    vips=np.sum(data['Pclass']==1)
    percentage=(float(vips)/891)*100
    assg_send(1, 3, str(rndr(percentage)))
    nnd(3)
    #4
    strt(4)
    mean=data['Age'].mean()
    med=data['Age'].median()
    assg_send(1, 4, str(mean)+' '+str(med))
    nnd(4)
    #5
    strt(5)
    cor=data.corr(method='pearson')
    assg_send(1, 5, str(cor['SibSp']['Parch']))
    nnd(5)
    #6
    strt(6)
    import re
    bag_of_words=[]
    for i in data['Name']:
        for n in i.split(' '):
            n=re.sub('[^a-zA-Z]', '', n)
            bag_of_words.append(n)
    d={}
    for word in bag_of_words:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    print [x+' '+str(d[x])+'\n' for x in sorted(d, key=d.get, reverse=True)]
    assg_send(1, 6, 'Mary')
    nnd(6)

def assignment2():
    import numpy as np
    import pandas
    from sklearn.tree import DecisionTreeClassifier
    data = pandas.read_csv('titanic.csv', index_col='PassengerId')
    new_data=data.loc[:, lambda data: ['Pclass', 'Fare', 'Age', 'Sex', 'Survived']]
    new_data=new_data.dropna(axis=0)
    data=new_data.loc[:, lambda data: ['Pclass', 'Fare', 'Age', 'Sex']]
    data['Sex']=data['Sex']=='female'
    target=new_data['Survived']
    clf=DecisionTreeClassifier(random_state=241)
    clf.fit(data, target)
    importances = clf.feature_importances_
    print importances
    prznks=['Pclass', 'Fare', 'Age', 'Sex']
    d={}
    for i in range(len(prznks)):
        d[prznks[i]]=importances[i]
    final=[x for x in sorted(d, key=d.get, reverse=True)]
    for i in final:
        print i, d[i]
    assg_send(2, 1, final[0]+' '+final[1])

assignment2()
    
