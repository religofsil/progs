# -*- coding: utf-8 -*-

import random, codecs

text=codecs.open('yoursin.txt', 'r', 'utf-8')
sins=[]
for line in text:
    sins.append(line)
print u'Покайся, дитя моё. Назови любой номер, и Господь укажет тебе твой грех.'
sin_number=input(u'Номер: ')
if sin_number not in range(1, 1025):
    sin_nimber=random.randint(1, 1024)
print ''
print u'Твой грех в том, что ты:\n'+sins[sin_number]
