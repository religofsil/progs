# -*- coding: utf-8 -*-

import os
import re
import codecs

f=codecs.open("dinocat.txt", "r", "utf8")
a=f.read()
word=raw_input(u"Введите слово: ")
w2=".+? .+? .+? .+? "+word+" .+? .+ .+ .+ "
conc=re.findall(w2, a)
print "c"
for i in conc:
    print i
print "a"
