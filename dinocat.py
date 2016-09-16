# -*- coding: utf-8 -*-

import codecs
import re

def mockingwiki(x, y, s):
    s2=re.sub (x, y, s)
    return s2

f=codecs.open("dinocat.txt", "r", "utf-8")
a=f.read()
a=mockingwiki(u"диноза́?вр", u"кот", a)
a=mockingwiki(u"Диноза́?вр", u"Кот", a)
f.close()
f2=codecs.open("cat-o-saur.txt", "w", "utf-8")
f2.write(a)
f2.close()
