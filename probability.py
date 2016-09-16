# -*- codecs: utf-8 -*-
import codecs, random
#random.shuffle(arr)
#орел -- 0.359

##arr=[1, 1, 1, 0]
##arr2=[]
##
##for i in range(100000):
##    x=random.choice(arr)
##    arr2.append(x)
##
##a=0
##
##for i in arr2:
##    a+=i
##
##print u"Вероятность выпадения орла: ", float(a)/100000
##print u"Вероятность выпадения решки: ", 1-float(a)/100000

arr=[]
arr2=[]
a=0

##for i in range(359):
##    arr.append(u"орел")
##for i in range(1000-359):
##    arr.append(u"решка")
##
##for i in range(10000000):
##    x=random.choice(arr)
##    arr2.append(x)
##
##for i in arr2:
##    if i==u"орел":
##        a+=1
##    else:
##        continue
##
##print u"Вероятность выпадения орла: ", float(a)/10000000
##print u"Вероятность выпадения решки: ", 1-float(a)/10000000

arr=[]
arr2=[]
f=codecs.open("long_poem.txt", "r", "utf-8")

for line in f:
    for i in line:
        arr2.append(i)
        if i not in arr:
            arr.append(i)

a=0
d={}
for i in arr:
    for n in arr2:
        if n==i:
            a+=1
    d[i]=a
    a=0

for i in d:
    if i in u"йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪЫВАПРФОЛДЖЭЯЧСМИТЬБЮ":
        print i, float(d[i])/len(arr2)
