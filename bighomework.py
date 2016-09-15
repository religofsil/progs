# -*- coding: utf-8 -*-
import random
import codecs

def firstword(txt):
    x=random.randint(0, 9)
    return txt[x]

def secword(txt):
    x=random.randint(10, 15)
    return txt[x]

def thirdword(txt):
    x=random.randint(57, 62)
    return txt[x]

def word4(txt):
    x=random.randint(16, 24)
    return txt[x]

def word5(txt):
    x=random.randint(64, 71)
    return txt[x]

def word21(txt):
    x=random.randint(72, 76)
    return txt[x]

def word22(txt):
    x=random.randint(6, 9)
    return txt[x]

def word23(txt):
    x=random.randint(25, 33)
    return txt[x]

def word24(txt):
    x=random.randint(39, 51)
    return txt[x]

def word25(txt):
    x=random.randint(54, 56)
    return txt[x]

def word26(txt):
    x=random.randint(77, 82)
    return txt[x]

def word27(txt):
    x=random.randint(83, 93)
    return txt[x]

def word27(txt):
    x=random.randint(83, 93)
    return txt[x]

def word31(txt):
    x=random.randint(94, 100)
    return txt[x]

def word32(txt):
    x=random.randint(101, 106)
    return txt[x]

def word33(txt):
    x=random.randint(52, 56)
    return txt[x]

def word41(txt):
    x=random.randint(107, 108)
    return txt[x]

def word42(txt):
    x=random.randint(109, 113)
    return txt[x]

def word51(txt):
    x=random.randint(114, 118)
    return txt[x]

def word52(txt):
    x=random.randint(34, 38)
    return txt[x]

def word53(txt):
    x=random.randint(120, 134)
    return txt[x]

def gensent1():
    sent=firstword(text)+" "+secword(text)+" "+thirdword(text)+u", потому что "+word4(text)+" "+word5(text)+"."
    return sent

def gensent2():
    sent=word21(text)+" "+word22(text)+" "+word23(text)+" "+word24(text)+", "+word25(text)+" "+word26(text)+u" начала "+word27(text)+"."
    return sent

def gensent3():
    sent=u"Но "+word31(text)+" "+word32(text)+", "+word33(text)+" "+word31(text)+" "+word32(text)+"."
    return sent

def gensent4():
    sent=u"После этого "+word31(text)+" "+word32(text)+u", но "+word41(text)+u" бы "+word31(text)+" "+word42(text)+" "+word27(text)+"?"
    return sent

def gensent5():
    sent=u"Тогда ведь "+word51(text)+u" бы "+word52(text)+" "+word24(text)+u", а это "+word53(text)+"."
    return sent

text=[]
f=codecs.open("pg2.txt", "r", "utf8")
for line in f:
    line=line.rstrip()
    text.append(line)
finaltext=[gensent1(), gensent2(), gensent3(), gensent4(), gensent5()]
a=" ".join(finaltext)
print a
