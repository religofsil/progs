#-*- coding: utf-8 -*-

import re
import codecs

'''r=re.search('[a-z][a-z][a-z]', 'abcd')
r.group() #до точки -- переменная, после точки -- ф-ция, кот. извлечет r
e=r.group()
print e
r=re.search('([a-z])([a-z])([a-z])([a-z])([a-z])([a-z])', 'abcdef')
f=r.group()
print f'''

f=codecs.open("flyingdeath.txt", "r", "utf-8")
for line in f:
    line = line.rstrip()
    phrases =  re.split ("([.,:;!?\(\)]+)|( and| or)", line)
    for i in phrases:
        if i != None:
            if re.search("(ha(ve)|s) [a-z]+ed", i):
                d = re.search("(ha(ve)|s) [a-z]+ed", i)
                a = d.group()
                print a
