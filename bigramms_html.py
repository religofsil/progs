# -*- coding: utf-8 -*-

##php -- код выполняется на сервере,
##пользователю выдается сгенерированная страница
##
##javascript -- код выполняется в браузере
##
##AJAX -- технология, позволяющая через javascript
##обращаться к серверу и заниматься там php
##
##css -- cascade style sheets (каскадные таблицы стиля)

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

a=opening("warnpeace.txt")
bigrarr=[("&"+a[i-1]+" "+a[i]) for i in range(1, len(a))]
word=raw_input(u"Введите слово: ").decode("cp1251")
bigrarr2=[]
for i in bigrarr:
    if "&"+word+" " in i or " "+word in i:
        i=re.sub("&", "", i)
        bigrarr2.append(i)
d={}
for i in bigrarr2:
    if i in d:
        d[i]+=1
    else: d[i]=1
red=[]
blue=[]
black=[]
for word in sorted(d, key=d.get, reverse=True):
    if d[word]>=5:
        word=word+"<br />"
        red.append(word)
    elif 1<d[word]<5:
        word=word+"<br />"
        black.append(word)
    elif d[word]==1:
        word=word+"<br />"
        blue.append(word)
r="".join(red)
bla="".join(black)
blu="".join(blue)
f2=codecs.open("hw.html", "w", "utf-8")
f2.write(u'<html><head></head><body><p style="color:red">'+r+'</p><p>'+bla+'</p><p style="color:blue">'+blu+'</p></body></html>')
f2.close()
