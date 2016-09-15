# -*- codecs: utf-8 -*-
import os, re, codecs, time
a=os.listdir('C:/Python27/progs/jeshlek_text_tagged')

def opening(x):
    f=codecs.open('jeshlek_text_tagged/'+x, "r", "utf-8")
    arr=[]
    for i in f:
        return i

arr=[]
for i in a:
    arr.append(opening(i))

arr3=[]
for i in arr:
    r=re.findall("{.+?}", i)
    for n in r:
        n=re.split("\|", n)
        for v in n:
            arr3.append(v)
            #print v
        
arr4=[]
arr5=[]
r2=re.compile("{.+\?(\+.+)=[A-Z].+}")
r3=re.compile("{(.+)\?\+.+=[A-Z].+}")
for i in arr3:
    a=r2.findall(i)
    b=r3.findall(i)
    for i in a:
        i=re.split("=.+}?", i)
        if i!=u"":
            arr4.append(i)
##        print "affix combination:"
##        print i
    for i in b:
##        print "stem:"
##        print i
        arr5.append(i)

d={}

r1=re.compile("=.+")
def mainfunc(*args):
    args=list(args)
    for i in range(20):
        a=raw_input("type smth, if you are done typing, press space, then enter: ")
        args.append(a)
        if a==' ':
            break
    args=tuple(args)
    d2={}
    paradigms=codecs.open("paradigms.csv", "w", "utf-8")
    for i in args:
        if i!=" ":
            d[i]=0
            for n in arr3:
                if i+"?" in n or i+"+" in n:
                    n=r1.sub("", n)
                    n=re.sub(u"{", "", n)
                    d[i]+=1
                    d2[n]=d[i]
    for i in sorted(d2):
        print i, d2[i]
        paradigms.write(i+"\t"+str(d2[i])+"\n")
    paradigms.close()
        


mainfunc() 
