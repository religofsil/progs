# -*- coding: utf-8 -*-
import re
import codecs

def opening(name, string):
    f = codecs.open(name, 'r', 'utf-8')
    f2=codecs.open(name+".csv", "w", "utf-8")
    for line in f:        
        line = line.rstrip()      
        words = line.split(string)
        for i in words:
            print i
        if len(words)==2:
            f2.write(words[0]+";"+string+";"+words[1]+"/n")
        elif len(words)==1:
            f2.write(words[0]+";"+string+"\n")

opening("sudya.txt", u"судя по всему")
