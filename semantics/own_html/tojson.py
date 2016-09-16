# -*- coding: utf-8 -*-
import codecs, json, re


def simplejj():
    txt = codecs.open('sintaksema.txt', 'r', 'utf-8')
    arr = []
    for line in txt:
        line = re.sub('\r\n', '', line)
        d = {}
        d['text'] = line
        arr.append(d)
    txt.close()
    jj = codecs.open('sintaxems.json', 'w', 'utf-8')
    json.dump(arr, jj, ensure_ascii=False, indent=2)
    jj.close()


def inliner(char, num, dict, line):
    dict[char] = line[num]


def opener():
    f = codecs.open('diffsintaxems.json', 'r', 'utf-8')
    print json.load(f, 'utf-8')


def cleverjj():
    txt = codecs.open('konstr.txt', 'r', 'utf-8')
    arr = []
    for line in txt:
        line = re.sub('\r\n', '', line)
        line = line.split('@')
        d = {}
        d['sint'] = line[0]
        d['semantics'] = line[1]
        inliner('verb', 2, d, line)
        inliner('verbsem', 3, d, line)
        inliner('prep', 4, d, line)
        inliner('noun', 5, d, line)
        inliner('nounsem', 6, d, line)
        inliner('case', 7, d, line)
        inliner('firstyear', 8, d, line)
        inliner('lastyear', 10, d, line)
        d['texts'] = [line[9], line[11]]
        arr.append(d)
    txt.close()
    jj2 = codecs.open('diffsintaxems.json', 'w', 'utf-8')
    json.dump(arr, jj2, ensure_ascii=False, indent=2)
    jj2.close()


opener()
