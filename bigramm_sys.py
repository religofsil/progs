# -*- coding: utf-8 -*-
import codecs
import re
import sys
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

a=opening("demon.txt")
arr=[a[i]+" "+a[i+1] for i in range(len(a)-1)]
numarr=[]
for i in arr:
    n=sum(1 for x in arr if x==i)
    numarr.append(n)
if max(numarr)>2:
    print u"Есть такая биграмма!"
else:
    print u"Нет такой биграммы."
