# -*- coding: utf-8 -*-
import codecs
import re
##a=["gyuky", "tsdtht", "nsdfc", "rkjbj"]
##bi={a[i]:a[i] for i in range (1, len(a))}
##for i in bi:
##    print i
##for x in 
##
##d={i[0:2]:i for i in a}
##for i in d:
##    print d[i]+" "+i

def opening(name):
    f = codecs.open(name, 'r', 'utf-8')
    arr=[]
    for line in f:        
        line = line.rstrip()
        a = re.sub(u'[,.?!:;—]', '', line)
        a = a.lower()        
        words = a.split(' ')
        for i in words:
            if len(i)>0:
                arr.append(i)
    return arr

a=opening("hearttransplant.txt")
##x=[i[1::2] for i in a]
##x=" ".join(x)
##print x

v=u"ёуеыаоэяию"
c=u"йцкнгшщзхфвпрлджчсмтб"
cv=[[c[n]+v[i] for i in range(len(v))] for n in range (len(c))]
arr=[]
arr2=[]
for i in cv:
    for x in i:
        for l in a:
            if x in l:
                arr.append(x+" is in our text")
            else:
                arr2.append(x+" is not in our text")
arr=set(arr)
arr2=set(arr2)
for i in arr:
    print i
for i in arr2:
    print i
