# -*- coding: utf-8 -*-
import codecs, json


def writedict(arr):
    f = codecs.open('slovar2.json', 'w', 'utf-8')
    d = {}  # финальный словарь
    subd=[] # служебный массив
    subd2={}
    arr.sort() # сортировка по тайским словам
    for i in arr:
        subd2[i]=[i.translation, i.pos, i.translit]
        subd.append([i.translation, i.pos, i.translit]) # делаем служебный словарь: каждому объекту ставим в соответствие перевод, часть речи и транслит
    keyss=[i.thaiword for i in arr]
    keyss=list(set(keyss))
    keyss.sort()
    count2=0
    for i in keyss:
        count2=keyss.index(i)
        d[i]={}
        count=1
        for n in subd[count2:-1]:
            if subd2[n].get().thaiword==i:
                d[i][count]=subd[n]
                count+=1
        print i, d[i]
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.close()


class Word:
    def __init__(self, thaiword, translation, pos, translit):
        self.thaiword = thaiword
        self.translation = translation
        self.pos = pos
        self.translit = translit

    def __gt__(self, other):
        return self.thaiword > other.thaiword

    def __lt__(self, other):
        return self.thaiword < other.thaiword


word1 = Word("yTHAIWORD", 'TRANSLATION', ['POS', 'hfkhg', 'vtyktk'], 'TRANSLIT')
word2 = Word("THAIWORD2", 'TRANSLATION2', ['POS2', 'kyfk'], 'TRANSLIT2')
word3 = Word("THAIWORD", 'TRANSLATION3', ['POS3'], 'TRANSLIT3')
word4 = Word("THAIWORD", 'TRANSLATION5', ['POS3'], 'TRANSLIT3')

writedict([word1, word2, word3, word4])
