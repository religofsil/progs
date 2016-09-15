# -*- coding: utf-8 -*-

import re
import codecs

count=0
countface=0
f=codecs.open("enets.xhtml", "r", "utf-8")
for line in f:
    line=line.rstrip()
    if re.search(u'subcol">[а-яА-Я]', line):
        count+=1
    if re.search(u'subcol.+[1-3](Sg|Pl|Du)', line):
        countface+=1
countface=countface/2
print u"переведенных слов:", count
print u"показателей лица:", countface
    
