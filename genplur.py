# -*- coding: utf-8 -*-

import codecs
import re

count=0
f = codecs.open("fiction3.xml", "r", "utf8")
for line in f:
    if re.search("pl.*gen", line):
        count+=1
        a=re.search(u"</ana>[а-яА-ЯЁё]*`[а-яё]*", line)
        if a!=None:
            l=a.group()
            l=l.replace("</ana>", "")
            print l
f.close()
print count
