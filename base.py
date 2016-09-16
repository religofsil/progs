# -*- coding: utf-8 -*-

import codecs
import re

arr=[]
f=codecs.open("ahlct007.xml", "r", "utf8")
for line in f:
    a=re.search(' [a-z]+ (<pause dur="[0-9]\.[0-9]"/> )?<shift feature="voice" new="laugh"/>', line)
    if a!=None:
        l=a.group()
        l=l.replace ('<pause dur="0.2"/>', '')
        l=l.replace ('<shift feature="voice" new="laugh"/>', '')
        l=l.replace (' ', '')
        arr.append(l)
f.close()
f2=codecs.open("base.txt", "w", "utf8")
for i in arr[:-1]:
    f2.write(i+", ")
f2.write(arr[-1])
f2.close()
