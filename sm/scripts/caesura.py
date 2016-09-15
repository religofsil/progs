# -*- coding:utf-8 -*-

import codecs
text = codecs.open("stih.txt", "r", "utf-8")
voc = [u'у', u'е', u'ы', u'а', u'о', u'э', u'я', u'и', u'ю', u'ё', u'У', u'Е', u'Ы', u'А', u'О', u'Э', u'Я', u'И', u'Ю', u'Ё']
i = 0
summa = []
stroca = 0
caesura = []

for line in text:
    stroca += 1
    syll = []
    #line = line.rstrip()
    word = line.split(" ")
    for hry in word:
        i=0
        let = list(hry)
        for ff in let:
            for vv in voc:
                if ff == vv:
                    i = i+1
        syll.append(i)
    j = 0
    for fox in range(0, (len(syll) - 1)):
        j += syll[fox]
        summa.append(j)

for a in summa:
    k = 0
    for b in summa:
        if a == b:
            k += 1
    if k == stroca:
        if a in caesura:
            continue
        else:
            caesura.append(a)
print caesura
        
        



                
        
