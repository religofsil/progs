# -*- coding: utf-8 -*-
import codecs
import re
import sys
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
##let=raw_input(u"Назови букву:").decode(sys.stdin.encoding)
##if any(i[-1]==let for i in a):
##    print u"Есть такая буква"
##else:
##    print u"Нет"
##print sum(1 for x in a if len(x)>2)
##print sum(len(x) for x in a if len(x)>2)
num=1
while type(num)!=None:
    num=input(u"Назови число: ")
    print sum(1 for x in a if len(x)==num)
