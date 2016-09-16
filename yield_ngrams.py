# -*- codecs: utf-8 -*-
import codecs

def xrange2(n):
    i=0
    while i<n:
        yield i
        i+=1

##for n in xrange2(100):
##    print n

def reademall():
    f=codecs.open("long_poem.txt", "r", "utf-8")
    for line in f:
        line=line.split(" ")
        for i in line:
            yield i

##for i in reademall():
##    print i

def get_ngrams(n):
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
                arr=" ".join(arr)
                yield arr
            a+=1
            
for i in get_ngrams(input("type a number: ")):
    print i
            
