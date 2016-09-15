# -*- codecs: utf-8 -*-

import re, codecs, time
re.compile(u"выражение", flags=re.U) #компилятор регулярных выражений
##Флаги: re.U, re.DOTALL
##re.DOTALL/
line2=u"erfuhi"
##m=r.search(line) #параметр -- то, В чем ищем выражение из re.compile

def howlong(func):
    t=0
    for i in range(100):
        t1=time.clock()
        func
        t2=time.clock()
        t=t+(t2-t1)
    t=t/100
    return u"время работы функции: "+str(t)

string=raw_input(u"Введите слово: ").decode("cp1251")

f=codecs.open("long_poem.txt", "r", "utf-8")
r=re.compile(u"[,?!.:]")
f2=[]
arr=[]
arr2=[]
def without():
    for line in f:
        line=re.sub(u'[,?!.:]', '', line)
        f2.append(line)
        if re.search(string[-3:]+"\n", line):
            arr.append(f2.index(line))
        if re.search(string+"\n", line):
            arr2.append(f2.index(line))
    return f2, arr, arr2

def withc():
    for line in f:
        line=r.sub('', line)
        f2.append(line)
        if re.search(string[-3:]+"\n", line):
            arr.append(f2.index(line))
        if re.search(string+"\n", line):
            arr2.append(f2.index(line))
    return f2, arr, arr2

withc()

for i in arr:
    if i-2 in arr2:
        print "yes"
        print f2[i-2]
        print f2[i]
    elif i-1 in arr2:
        print "yes"
        print f2[i-1]
        print f2[i]
    elif i+1 in arr2:
        print "yes"
        print f2[i]
        print f2[i+1]
    elif i+2 in arr2:
        print "yes"
        print f2[i]
        print f2[i+2]

f2=[]
arr=[]
arr2=[]

print u"без компиляции", howlong(without)
print u"с компиляцией", howlong(withc)
