# -*- coding:utf-8 -*-
import re
import codecs
import os

def opentext():
    f=codecs.open("examfile.txt", "r", "utf-8")
    a=f.read()
    return a

a=opentext()
years=re.findall(u"(?: [1-2]?[0-9]?[0-9][0-9] г(?:(?:\\.)|(?:од[а-я]?[а-я]?)) (?:(?:до)? н\\.э\\.)?)", a)
for i in years:
    print i
interv=re.findall(u"([1-2]?[0-9][0-9][0-9])(?:-|—)([1-2]?[0-9]?[0-9][0-9])", a)
for i in interv:
    for n in i:
        if n!="31":
            print n

alldates=[]
a1=re.findall(u"[1-3]?[0-9] [а-я]{,10} [1-2]?[0-9][0-9][0-9]", a)
a2=re.findall(u"[1-3]?[0-9]\\.[0-1][1-2]\\.[1-2][0-9][0-9][0-9]", a)
a3=re.findall(u"[XIVLMC][XIVLMC]?[XIVLMC]? в?в\\.", a)
a4=re.findall(u"(?: [1-2]?[0-9]?[0-9][0-9] (?:г(?:(?:\\.)|(?:оду?о?м?))?) (?:(?:до)? н\\.э\\.)?)", a)
a5=re.findall(u"[1-2]?[0-9]?[0-9][0-9]-[ехм]и?", a)
alldates.append(a1)
alldates.append(a2)
alldates.append(a3)
alldates.append(a4)
alldates.append(a5)
d={}
for i in alldates:
    for l in i:
        d[l]=0
        r=re.findall(l, a)
        d[l]=len(r)
f2=codecs.open("examresults.csv", "w", "utf-8")
for i in d:
    f2.write(i+"'"+str(d[i])+"\n")
f2.close()

num=[]
for i in years:
    num1=re.findall(u"[1-2]?[0-9]?[0-9][0-9]", i)
    for k in num1:
        num.append(k)
vek=[]
for i in num:
    i2=int(i)
    i2=i2/100+1
    vek.append(i2)
    
for i in vek:
    os.makedirs(i)
