# -*- coding: utf-8 -*-
import codecs
import re
def opening(name):
    f = codecs.open(name, 'r', 'utf-8')
    arr=[]
    for line in f:        
        line = line.rstrip()
        a = re.sub(u'[,.?!:;—]', '', line)
        a = a.lower()        
        words = a.split(' ')
        for i in words:
            if len(i)>0:
                arr.append(i)
    return arr

a=opening("hearttransplant.txt")
#for i in a:
   # print i
arl=[]
for i in a:
    arl.append(len(i))

print u"длина максимального слова:"
print max(arl)
print u"длина минимального слова:"
print min(arl)
