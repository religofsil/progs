import os, re, codecs, time

a=os.listdir('C:/Python27/progs/jeshlek_text_tagged')
def opening(x):
    f=codecs.open('jeshlek_text_tagged/'+x, "r", "utf-8")
    arr=[]
    for i in f:
        return i
t=0
t1=time.clock()
arr=[]
for i in a:
    arr.append(opening(i))

arr2=[]
for i in arr:
    a=re.sub("{.+?}", "", i)
    a=a.split()
    for n in a:
        if n[-1] not in "1234567890-" and n[0] not in "1234567890-":
            arr2.append(n)

arr2=set(arr2)
f2=codecs.open("words.txt", "w", "utf-8")
for i in arr2:
    f2.write(i+"\n")
    
t2=time.clock()
t=t+(t2-t1)
print "words per second: "+str(1/t)

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
for i in arr3:
    a=re.findall("{.+\?(\+.+)=[A-Z].+}", i)
    b=re.findall("{(.+)\?\+.+=[A-Z].+}", i)
    for i in a:
        i=re.sub("=.+}?", "", i)
        i=re.sub("\+", "", i)
        arr4.append(i)
        print "affix combination:"
        print i
    for i in b:
        print "stem:"
        print i
        arr5.append(i)

arr6=[]
for i in arr4:
    for l in arr5:
        if i==l:
            print i
            arr6.append(i)
if len(arr6)==0:
    print u"я не нашла таких основ и аффиксов"
