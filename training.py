# -*- coding: utf-8 -*-
import random
import codecs

def hokku1(txt):
    x=random.randint(0, 8)
    return txt[x]

def hokku2(txt):
    x=random.randint(9, 17)
    return txt[x]

def hokku3(txt):
    x=random.randint(18, 28)
    return txt[x]

text=[]
f=codecs.open("pg.txt", "r", "utf8")
for line in f:
    line=line.rstrip()
    text.append(line)
hokk=hokku1(text)+"\n"+hokku2(text)+"\n"+hokku3(text)
print hokk
