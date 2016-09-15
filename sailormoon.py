# -*- coding: utf-8 -*-

import codecs
import re

def getsmth(x, y):
    s=re.findall (x, y)
    return s

def writeall():
    writesmth(year)
    writesmth(name)

def readsmth():
    f=codecs.open("sailormoon.txt", "r", "utf-8")
    a=f.read()
    return a

def writesmth(x):
    f2=codecs.open("chinaresults.txt", "a", "utf-8")
    for i in x:
        f2.write(i+"\n")
    f2.write("\n")

def andbiblical(y):
    f=codecs.open("holychinesebible.txt", "w", "utf-8")
    y2=re.sub(u"((?:\\r\\n)|\\. )(«?[А-Я])", u"\\1 И \\2", y)
    f.write(y2)
    f.close()
    
a=readsmth()
year=getsmth(u" ((?:1|2)[0-9]{3})", a)
name=getsmth(u'«[А-ЯЁ][а-яё]{,15}(?:-[0-9])?»', a)
#for i in name:
    #print i
year.sort()
#writeall()
andbiblical(a)
x=re.findall(u"\\. «?[А-Я]", a)
for i in x:
    print x
