# -*- coding: utf-8 -*-
import codecs
import re

def opening(name):
    f = codecs.open(name, 'r', 'cp1251')
    arr=[]
    for line in f:
        arr.append(line)
    return arr

a=opening ("zags2013.csv")
a=set(a)
b=opening ("zags2012.csv")
b=set(b)
c=a-b
print u"в 2012 году были популярны имена:"
for i in c:
    print i
