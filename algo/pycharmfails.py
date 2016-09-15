# -*- coding: utf-8 -*-
import re, math, codecs, logging


def wordbag(docs):
    arr = []
    for i in docs:
        i = i.split()
        for l in i:
            l = l.lower()
            l = re.sub(u'[^а-яa-z]', '', l)
            if l != '':
                arr.append(l)
    return arr


def tf(docs):
    arr = wordbag(docs)
    d = {}
    for x in arr:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d


def idf(docs):
    arr = wordbag(docs)
    arrs = [wordbag([doc]) for doc in docs]
    d = {}
    for i in arr:
        d[i] = 0
        for doc in arrs:
            if i in doc:
                d[i] += 1
    for i in d:
        d[i] = math.log(d[i])
    return d


def finder(docs, word):
    arrs = [wordbag([doc]) for doc in docs]
    for i in arrs:
        if word in i:
            print word, arrs.index(i) + 1


def main():
    doctitles = ['tfidf' + str(i) + '.txt' for i in range(1, 6)]
    docs = []
    for i in doctitles:
        f = codecs.open(i, 'r', 'utf-8')
        text = f.read()
        docs.append(text)
        f.close()
    tf = codecs.open('tf.txt', 'w', 'utf-8')
    tf.close()
    for i in [u'linux', u'софт', u'программы', u'система', u'технологии', u'it']:
        finder(docs, i)

def wordbagAdj():
    f=codecs.open('chunk-500.txt', 'r', 'utf-8-sig')
    arr=[]
    count=1
    for line in f:
        arr.append(re.split('(?:  )|(?:, )|(?:\. )', line))
        print count
        count+=1
    f.close()
    arr2=[]
    for i in arr:
        a=[]
        for n in i:
            try:
                if len(n.split(' '))<=4:
                    a.append(n)
            except:
                pass
        arr2.append(a)
    return arr2

def tfAdj(arr):
    print len(arr)
    d={}
    for i in arr:
        for n in i:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
    for x in sorted(d, key=d.get(), reverse=True):
        print x, d[x]

tfAdj(wordbagAdj())
