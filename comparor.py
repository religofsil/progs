# -*- coding:utf-8 -*-
import codecs


def comparison(file1, file2):
    from nltk.metrics import distance as dst
    f1 = codecs.open(file1, 'r', 'utf-8')
    text1 = f1.read()
    t1 = text1.split()
    d1=freqdict(t1)
    f1.close()
    f2 = codecs.open(file2, 'r', 'utf-8')
    text2 = f2.read()
    print dst.binary_distance(text1, text2)
    t2 = text2.split()
    d2 = freqdict(t2)
    text1 = text1.split(' ')
    text2 = text2.split(' ')
    f2.close()
    arr = []
    for i in text1:
        if i not in text2:
            arr.append(i)
    for i in arr:
        print i
    print len(arr)
    print len(text2)
    print 'by words: ', float(len(arr)) / len(text2)
    arr2=[]
    for i in t1:
        if i not in t2:
            arr2.append(i)
    print 'by symbols: ', float(len(arr2)) / len(t2)


def freqdict(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


comparison('cleanishcorp.txt', 'newcleancorp.txt')
