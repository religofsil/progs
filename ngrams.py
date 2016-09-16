# -*- codecs: utf-8 -*-
import codecs

def get_ngrams(n, w):
    f=codecs.open("long_poem.txt", "r", "utf-8")
    for line in f:
        line=line.split(" ")
        a=0
        while a<len(line):
            arr=[]
            for i in line[a:n+a]:
                if i:
                    arr.append(i)
            if len(arr)==n:
                if w in arr:
                    arr=" ".join(arr)
                    yield arr
            a+=1

def howmuch(i, arr):
    a=0
    for n in arr:
        if i==n:
            a+=1
    return a

arr=[]

for i in get_ngrams(input("type a number: "), raw_input("type a word: ").decode("cp1251")):
    arr.append(i)

d={}
for i in arr:
    d[i]=howmuch(i, arr)

n=dict.keys(d)
f=[]
for i in sorted(n, key=d.get, reverse=True):
    f.append(d[i])

l=raw_input("guess: ").decode("cp1251")
if l in d and d[l]==f[0]:
    print "you're right!"
else:
    print "you're wrong!"
    a=""
    for i in d:
        if d[i]==f[0]:
            a=i
    print "the correct answer is", a

