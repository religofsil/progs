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

e=" "
emas=[]
while e!="":
    e=raw_input("type your word: ").decode("cp1251")
    emas.append(e)
else:
    emass=[]
    esch=[]
    eschet=1
    for e in emas:
        z=0
        e=list(e)
    while z<=len(e):
        if e[z] not in emass:
            emass.append(e[z])
            esch.append(eschet)
            eschet+=1
        else:
            emass.append("")
            esch.append("")
            eschet+=1
        z+=1
    v=" ".join(e)
                                           
