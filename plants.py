# -*- coding: utf-8 -*-
import re
import codecs

l=0
arr=[]
f=codecs.open("file.htm", "r", "utf8")
for line in f:
    arr.append(line)
f.close()
while l<len(arr):
    if re.search (u"Семейство", arr[l]):
        phrases=re.split("[<>]", arr[l+1])
        for i in phrases:
            if i!=None:
                d=re.match(u"[а-яА-ЯЁё]+", i)
                if d!=None:
                    a=d.group()
                    print d.group()
                    f2=codecs.open("families.txt", "a", "utf8")
                    f2.write(d.group())
                    f2.close
    l+=1
