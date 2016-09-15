# -*- coding: utf-8 -*-
a=[]
stroka="0"
while stroka!="":
    stroka=raw_input(u"введите слово, пожалуйста: ").decode("cp1251")
    if stroka!="":
        a.append(stroka)
else:
    for word in a:
        boxforletters=""
        for letter in word:
            for h in range (0, 3):
                boxforletters+=letter
        print boxforletters
