# -*- coding: utf-8 -*-
import codecs
l=[]
f=codecs.open("test.txt", "r", "utf-8-sig")
for line in f:
    line=line.rstrip()
    l.append(line)
i=1
while i<len(l)-1:
    print l[i]
    i+=2

mass=[]
schet=[]
schetchik=1
for line in l:
    d=0
    while d<=len(line):
        if line[d] not in mass:
            mass.append(line[d])
            schet.append(schetchik)
            schetchik+=1
            print mass[d], schetchik
        else:
            mass.append("")
            schet.append("")
            schetchik+=1
        d+=1
