# -*- coding: utf-8 -*-

import os
import re
import codecs

#взаимодействие с операционной системой

##'''os.makedirs('example\\1\\2\\3') #создание папки 3 в папке 2 в папке 1 в папке example в папке программы (все папки создаются)
##os.getcwd() #выдает адрес рабочей директории
##a=os.listdir('.') #выдает массивом каталог всех папок рабочей директории
##os.path.exists('D:\\example') #проверяет путь на существование
##os.path.detsize('D:\\example\text.txt') #выдает размер файла
##for root, dirs, files in os.walk(u'.'):'''
##'''c=[]
##for fl in a:
##    f=open(fl)
##    cnt=f.read()
##    f.close()
##    c.append(cnt)''' #считывает все файлы из папки


f=codecs.open("warnpeace.txt", "r", "cp1251")
a=f.read()
parts=re.split(u"ЧАСТЬ", a)
parts=parts[1::]
prtnum=0
for prt in parts:
    chapters=re.split(u"\\r\\n\\r\\n[IVXLMC]{,4}\\r\\n\\r\\n", prt)
    prtnum+=1
    prts=str(prtnum)
    chptnum=0
    chapters=chapters[1::]
    for chpt in chapters:
        chptnum+=1
        chpts=str(chptnum)
        pth="C:\\Python27\\progs\\Tolstoy\\"+prts+"\\"+chpts+"\\"
        os.makedirs(pth)
        f2=codecs.open(pth+"text.txt", "w", "cp1251")
        f2.write(chpt)
        f2.close()
f.close()
