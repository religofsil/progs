# -*- coding: utf-8 -*-
words={u'мама':0.5, u'мыла':0.01, u'вещи':0.3}
probabilities


def viterbi():
    pass

def chooser(**kwargs):
    arr=[]
    d={}
    for i in kwargs:
        arr.append(i[0]*i[1])
        d[arr[-1]]=i
    return d[max[arr]], max(arr)