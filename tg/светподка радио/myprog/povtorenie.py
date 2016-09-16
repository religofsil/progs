#-*- coding:utf-8 -*-
import os
import codecs
import re
def main():
    arr = []
    for root, dirs, files in os.walk(u'C:\\Танька\\put\\mir\\Tom1\\'):
        for oneFile in files:
            #print root
            #print oneFile
            fileName = root + u'\\' + oneFile
            f = codecs.open(fileName, 'r', 'utf-8')
            s = f.read()
            #print s
            arr.append(s)
            f.close()
    return arr
def chastota(d):
    slovar = {}
    znaki = ['!', '?', '[', ']', '(', ')', ':', ';', '"', "'", '*', '.', ',', '--']
    for i in d:
        spisok_slov = i.split(' ')
        for slovo in spisok_slov:
            slovo = slovo.lower()
            for zn in znaki:
                slovo = slovo.replace(zn, '')
            if re.search(u'[a-z]', slovo):
                pass
            elif slovo != '':
                #print u'proveriaem slovo'
                if slovo in slovar:
                    slovar[slovo] += 1
                    #print slovo
                else:
                    slovar[slovo] = 1
                    #print u'proveriaem slovo2'
    #print slovar[u'я']
    s = codecs.open('put.txt', 'w', 'utf-8')
    for slovo in sorted(slovar, key=slovar.get, reverse=True):
        s.write(slovo + ' - ' + str(slovar[slovo]) + '\n')
    s.close()
d = main()
chastota(d)
