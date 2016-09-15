# -*- coding: utf-8 -*-
import urllib2
import re
import codecs
import os

def opening(name):
    f = codecs.open("corpora/"+name, 'r', 'utf-8')
    arr=[]
    for line in f:        
        line = line.rstrip()
        a = re.sub(u'[\\\,|.?$!:\^;—0-9\'"\(\)*@_\#%\-]', ' ', line)
        a = a.lower()        
        words = a.split()
        for i in words:
            if len(i)>0:
                arr.append(i)
    return arr

arr=[]
for name in os.listdir("corpora"):
    a=opening(name)
    a=set(a)
    arr.append(a)
textarr=[]
for i in arr:
    for l in i:
        textarr.append(l)
textarr=set(textarr)
print u"Количество словоупотреблений:", len(textarr)

count=0
for a in arr:
    if any(i==u"и" for i in a):
        count+=1
if count==19:
    print u'Везде есть союз "и"'
else:
    print u'Не везде есть союз "и"'
    
count=0
for a in arr:
    if any(i[0]==u"я" for i in a):
        count+=1
if count>0:
    print u'Есть слово на букву "я"'
else:
    print u'Нет слова на букву "я"'

for i in range(1, len(arr)):
    arr[i]=arr[i]&arr[i-1]
print u"Слова, которые есть везде:"
for i in arr[-1]:
    print i
