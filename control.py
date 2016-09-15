# -*- coding: utf-8 -*-

import codecs
import re

countpunct=0
gen=0
d={}
f=codecs.open("island.xml", "r", "utf8")
for line in f:
    if re.search('<c type="punctuation">', line):
                 countpunct+=1
    if re.search('<w lemma=', line):
        line=line.rstrip()
        if line not in d:
            d[line]=1
        else:
            d[line]+=1
    if re.search('type="n..e', line):
        gen+=1
f2=codecs.open("results.txt", "a", "utf8")
f2.write(str(countpunct)+"\n")
for st in sorted(d,key=d.get):
    f2.write(st+" -- "+str(d[st])+u" шт\n")
f2.write(u"родительных падежей: "+str(gen))
