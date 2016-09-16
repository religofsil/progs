# -*- coding: utf-8 -*-
import urllib2
import re
import codecs
import HTMLParser
##hPrs=HTMLParser.HTMLParser()
##text=hPrs.unescape(u"&nbsp;&laquo;z") #преобразует символы в кавычках
##print text
##req=urllib2.Request("http://newsru.com", headers={"UserAgent":"Mozilla 5.0"})
site="http://newsru.com"
def gotorefs(url):
    req=urllib2.Request(url, headers={"UserAgent":"Mozilla 5.0"})
    r=urllib2.urlopen(req).read()
    n=[]
    a=re.findall('href="(http://.+?)"', r)
    for i in a:
        n.append(i)
    return n
v=gotorefs(site)
x=[]
for i in v:
    x.append(gotorefs(i))
for i in x:
    for l in i:
        print l
print 8
