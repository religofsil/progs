# -*- coding: utf8 -*-

import random

def rand_word(n):
    r=random.randint(0, len(n)-1)
    return n[r]


def sent1():
    for arr in words:
        w=rand_word(arr)
        string.append(w)
    s=" ".join(string)
    return s

def sent1_2():
    for arr in words:
        w=rand_word(arr)
        string.append(w)
    s=" ".join(string)
    return s

def sent2():
    for arr in q_words:
        w=rand_word(arr)
        string.append(w)
    s=u"кто "+" ".join(string)+"?"
    return s

def sent3():
    l=u"пока "+sent1()+u", "+sent1_2()
    return l

words1=[u"человек", u"кот", u"семья", u"холодильник"]
words2=[u"стоит", u"пьёт", u"спивается"]
words3=[u"на кухне", u"в лесу", u"в комнате"]
words4=[u"тихо", u"медленно"]
words=[words1, words4, words2, words3]
q_words=words[1:-1]
string=[]

des=random.randint(0, 2)
print des
if des==0:
    f=sent1()
elif des==1:
    f=sent2()
elif des==2:
    f=sent3()
print f
