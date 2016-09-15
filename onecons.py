# -*- coding: utf-8 -*-
import codecs
import re

def leaveonecons(a):
    a2=re.sub(u"([цкнгшщзхфвпрлджчсмтбйьъЬЪЙЦКНГШЩЗХФВПРЛДЖЧМСТБ])[цкнгшщзхфвпрлджчсмтбйьъЬЪЙЦКНГШЩЗХФВПРЛДЖЧМСТБ][цкнгшщзхфвпрлджчсмтбйьъЬЪЙЦКНГШЩЗХФВПРЛДЖЧМСТБ]?[цкнгшщзхфвпрлджчсмтбйьъЬЪЙЦКНГШЩЗХФВПРЛДЖЧМСТБ]?", u"\\1", a)
    return a2

def openwriteclose():
    f=codecs.open("sailormoon.txt", "r", "utf-8")
    a=f.read()
    a=leaveonecons(a)
    f2=codecs.open("onecons.txt", "w", "utf-8")
    f2.write(a)
    f.close()
    f2.close()

openwriteclose()
