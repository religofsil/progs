# -*- coding: utf-8 -*-
a=[]
b="0"
while b!="":
    b=raw_input(u"Введите, пожалуйста, слово: ").decode("cp1251")
    if b!="":
        a.append(b)
else:
    for i in range (0, 8):
        for j in a:
            n=len(j)
            if n==i:
                print j
