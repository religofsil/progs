#-*- coding:utf-8 -*-
import codecs
f=codecs.open('7.txt','r','utf-8')
one=0
three=0
for i in f:
    i=i.rstrip()
    #print(i)
    sp=i.split(' ')
    for j in range(0,len(sp)):
        if len(sp[j])==1:
            one+=1
        elif len(sp[j])==3:
            three+=1
f.close()
#print(one)
#print(three)
if one==0:
    print(u'Нет слов длины 1! :(')
else:
    three=float(three)
    one=float(one)
    print(u'Слов длины 3 больше слов длины 1 в следующее количество раз:')
    print(three/one)
