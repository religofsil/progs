# -*- coding: utf-8 -*-
import codecs, json


def writedict(arr):
    f = codecs.open('slovar2.json', 'w', 'utf-8')
    d = {}  # финальный словарь
    subd = []  # служебный массив
    subd2 = {}  # служебный словарь
    arr.sort()  # сортировка по тайским словам
    for i in arr:
        print i.thaiword
        subd2[i] = [i.translation, i.pos,
                    i.translit]  # делаем служебный словарь: каждому объекту ставим в соответствие перевод, часть речи и транслит
        subd.append(
            [i.translation, i.pos, i.translit])  # делаем служебный массив значений, отсортированный по тайским словам
    print '---------------------------'
    keyss = [i.thaiword for i in arr]
    keyss = list(set(keyss))
    keyss.sort()  # отсортированный массив тайских слов
    print keyss
    print '---------------------------'
    count2 = 0
    print [n.translation for n in arr]
    print '---------------------------'
    for i in keyss:
        print '---------------------------'
        c = 1
        d[i] = {}
        print i, d[i]
        print '---'
        for n in arr[count2::]:
            print 'starting with a word ', count2
            if i == n.thaiword:
                d[i][c] = [n.translation, n.pos, n.translit]
                print i, d[i]
                c += 1
            else:
                count2 = arr.index(n)
                print "i'm breaking ", count2
                break
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
