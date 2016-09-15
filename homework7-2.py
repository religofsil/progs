# -*- coding: utf-8 -*-
import codecs
f=codecs.open("file.txt", "r", "utf-8-sig")
n=0.0
m=0.0
for line in f:
    line=line.rstrip()
    words=line.split(" ")
    for word in words:
        m+=1
        if len(word)>10:
            n+=1
if n!=0:
    b=n*100/m
    a=round (b, 2)
    print a
else: print ("all words are shorter than 10")
