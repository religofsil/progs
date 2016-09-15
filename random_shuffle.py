# -*- coding:utf-8 -*-
import re
import codecs
import random

def shuffle (x):
    letrus=u"йцукенгшщзхъфывапролджэячсмитьбюё"
    def randlet (a):
        l=random.randint(0, len(a)-1)
        return a[l]
    i=0
    while i<len(x)/2:
        x=re.sub(randlet(x), randlet(letrus), x)
        i+=1
    return x

def opening(name):
    f = codecs.open(name, 'r', 'utf-8')
    arr=[]
    for line in f:        
        line = line.rstrip()
        a = re.sub(u'[\«\»,.?!:;—-]', '', line)
        a = a.lower()        
        words = a.split(' ')
        for i in words:
            if len(i)>0:
                arr.append(i)
    return arr

a=opening("hearttransplant.txt")
d={i:shuffle(i) for i in a}
for i in d:
    print i+" "+d[i]
