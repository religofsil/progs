# -*- coding: utf-8 -*-
import urllib2
import re
import codecs
import os

if os.path.exists("corpora")==False:
    os.makedirs("corpora")
site="http://www.newsru.com/dossier/5837.html"

def gotorefs(url):
    req=urllib2.Request(url, headers={"UserAgent":"Mozilla 5.0"})
    r=urllib2.urlopen(req).read()
    n=[]
    a=re.findall('href="(/cinema/[0-9A-Za-z]+/[0-9A-Za-z]+.html)"', r)
    for i in a:
        i="http://www.newsru.com"+i
        n.append(i)
    return n

v=gotorefs(site)
x=[]
a=0
for i in v:
    if a<60:
        x.append(i)
    else: break
    a+=1
x=set(x)
l=1
for i in x:
    print i
    n="C:\Python27\progs\corpora\\"+str(l)+'.txt'
    f=codecs.open(n, "w", "utf-8")
    req=urllib2.Request(i, headers={"UserAgent":"Mozilla 5.0"})
    r=urllib2.urlopen(req).read().decode("cp1251")
    r=re.sub('<.+?>', "", r)
    r=re.sub('[a-zA-Z&+/=><\[\]\{\}]', "", r)
    f.write(r)
    f.close()
    l+=1
