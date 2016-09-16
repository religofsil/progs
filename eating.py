#-*- coding: utf-8 -*-

import re
import codecs

i=1

f=codecs.open("file.txt", "r", "utf-8")
for line in f:
    line=line.rstrip()
    words=line.split(" ")
    for word in words:
        if re.search(u'съе(вш(ая|ую|е(го|е|й|му?)|и(е|й|ми?|х))|д(и(м|те)|ят|ен(а|о|ы|н((ая|ую|о(го|е|й|му?|ю))|ы(е|й|ми?|х)))?)|л(а|и|о)?|м|сть?|в|шь(те)?)', word):
            print i, word
            i+=1
f.close()
