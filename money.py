# -*- coding: utf-8 -*-

import codecs
import re

f=codecs.open("rur.txt", "r", "utf8")
a=f.read()
sent=re.split(u"\.", a)
for i in sent:
    c=re.findall(u' (?:Я|я) (?:.+)?(не [а-яѣ]+[глжн][ъую])[,.?! ]', a)
f.close()
f2=codecs.open("resur.txt", "w", "utf8")
for l in c:
    f2.write(l+"\n")
f2.close()
