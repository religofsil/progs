# -*- coding: utf-8 -*-

import codecs
import re
import random

def word_sasha():
    arr = []
    f = codecs.open('text1.txt', 'r', 'utf-8')
    aa = f.read()
    a = re.sub(u' +|\r\n', u' ', aa, flags = re.U) 
    f.close()
    znaki = ['!', '?', '[', ']', '(', ')', ':', ';', '"', "'", '*', '.', ',']
    spisok_slov = a.split(' ')
    for slovo in spisok_slov:
        slovo = slovo.lower()
        for zn in znaki:
            slovo = slovo.replace(zn, '')
        arr.append(slovo)
    return arr

def bigramm():
    arr = word_sasha()
    bi = [(arr[i - 1] + ' ' + arr[i]) for i in range(1, len(arr))]
    return bi

def poisk():
    res = []
    arr = bigramm() 
    word = raw_input(u'Введите слово: ').decode('cp1251')
    for i in arr:
        new = i.split(' ')
        if word == new[0]:
            res.append(new[1])
    return res

def dik_and_html():
    arr = poisk()
    d = {}
    a1 = []
    b1 = []
    for slovo in arr:
        if slovo in d:
            d[slovo] += 1
        else:
            d[slovo] = 1
    s = codecs.open('put_Mart.html', 'w', 'utf-8')
    for slovo in sorted(d, key=d.get, reverse=True):
##        print d[slovo]
##        print slovo + ' - ' + str(d[slovo]) + '\n'
        if d[slovo] > 2:
            a1.append(slovo)
        else:   
            b1.append(slovo)
    for i in a1:
        s.write(u'<html><head><title>homework</title></head><body><p><span style = "color:red">' + i + u'</span></p></body></html>')
    for i in b1:
        s.write(u'<html><head><title>homework</title></head><body><p><span style = "color:blue">' + i + u'</span></p></body></html>')
        
dik_and_html()
     
    
            
