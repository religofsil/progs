# -*- coding: utf-8 -*-
import codecs
import re

def opening(name):
    f = codecs.open(name, 'r', 'utf-8')
    arr=[]
    for line in f:
        arr.append(line)
    return arr

def findname(array, pattern):
    arr=[]
    for i in array:
        a=re.findall(pattern, i)
        arr.append(a)
    return arr

arr=opening("girlsnames.htm")
arr2=findname(arr, u'<p align="center" style="text-align: center;">([А-Я][а-яё]+(?:, [А-Я][а-яё]+)?)')
arr3=[]
for i in arr2:
    for l in i:
        arr3.append(l)
arr2010=arr3[::5]
arr1991=arr3[4::5]
set2010=set(arr2010)
set1991=set(arr1991)
s=set2010&set1991
unic1991=set1991-set2010
unic2010=set2010-set1991
print u"В обоих списках встречаются имена:"
for i in s:
    print i
print u"Для 1991 года уникальны имена:"
for i in unic1991:
    print i
print u"Для 2010 года уникальны имена:"
for i in unic2010:
    print i
