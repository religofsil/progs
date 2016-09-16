# -*- coding: utf-8 -*-
import re, math, codecs


def wordbag(docs):
    arr = []
    for i in docs:
        i = i.split()
        for l in i:
            l = l.lower()
            l = re.sub(u'[^а-яёa-z]', '', l)
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
        d[i] = math.log(len(arrs)/d[i])
    return d


def tfidf(dict1, dict2):
    d = {}
    for i in dict1:
        d[i] = dict1[i] * dict2[i]
    return d


def finder(docs, word):
    arrs = [wordbag([doc]) for doc in docs]
    for i in arrs:
        if word in i:
            print word, arrs.index(i) + 1


def filewriter(filename, dict):
    f = codecs.open(filename, 'w', 'utf-8')
    for i in sorted(dict, key=dict.get, reverse=True):
        f.write(i + ' ' + str(dict[i]) + '\r\n')
    f.close()


def tablemaker(words, docs, doctitles):
    words=list(set(words))
    table=codecs.open('termdocmatrix.csv', 'w', 'utf-8')
    titlestring=';'
    for n in doctitles:
        titlestring=titlestring+n
        titlestring=titlestring+';'
    table.write(titlestring+'\n')
    for i in words:
        s=i+';'
        for doc in docs:
            if i in doc:
                s+='1;'
            else:
                s+='0;'
        table.write(s+'\n')
    table.close()



def main():
    doctitles = ['tfidf' + str(i) + '.txt' for i in range(1, 6)]
    docs = []
    for i in doctitles:
        f = codecs.open(i, 'r', 'utf-8')
        text = f.read()
        docs.append(text)
        f.close()
    for i in [u'linux', u'софт', u'программы', u'система', u'технологии', u'it']:
        finder(docs, i)
    filewriter('tf.txt', tf(docs))
    filewriter('tf-for-1.txt', tf([docs[3]]))
    filewriter('idf.txt', idf(docs))
    filewriter('tfidf.txt', tfidf(tf(docs), idf(docs)))
    #tablemaker(wordbag(docs), [wordbag([doc]) for doc in docs], doctitles)


main()
