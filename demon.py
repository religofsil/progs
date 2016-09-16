##В множестве элементы не нумерованы и не повторяются.
##Могут храниться разные типы данных.
##Множество делается из массива функцией set.
##множество 1 | множество 2 == множество 1+2
##множество 1 & множество 2 == пересечение 1 и 2
##множество 1 - множество 2 == множество 1-2
##множество 1 ^ множество 2 == сумма минус два пересечения

# -*- coding: utf-8 -*-
import codecs
import re

def opening(name):
    f = codecs.open(name, 'r', 'utf-8')
    arr=[]
    for line in f:        
        line = line.rstrip()
        a = re.sub(u'[,.?!:;-]', '', line)
        a = a.lower()        
        words = a.split(' ')
        return words

a=opening("file.txt")
a=set(a)
for x in a:
    print x

print 8
