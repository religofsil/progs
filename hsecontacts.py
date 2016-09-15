# -*- coding: utf-8 -*-

import codecs
import re

f=codecs.open("hsecontacts.htm")
a=f.read()
c=re.findall(u'<a href="mailto:(?:[a-zA-Z0-9_]+)@(?:[a-zA-Z0-9]+\....?.?)">((?:[a-zA-Z0-9_]+)@(?:[a-zA-Z0-9]+\....?.?))</a>', a)
#print c

f3=codecs.open("ot4est.htm", "r", "cp1251")
l=f3.read()
o=re.findall(u'([А-Я][а-я]+(?:о|е)в(?:(?:н[аеыу])|ич(?:[ауе]?м?)))', l)
for i in o:
    print i

f.close()
f2=codecs.open("hsecont.txt", "w", "utf8")
for i in c:
    f2.write(i+"\r\n")
f2.close()
