# -*- codecs: utf-8 -*-
import codecs, random, re

f=codecs.open("Master_EN.txt", "r", "utf-8")

arrlet=[]
arrlen=[]
arr=[]
arr2=[]

for line in f:
    line=line.lower()
    line=re.sub(u"[—\.,!?\"»«…:]", "", line)
    line=re.sub(u"-", " ", line)
##    for i in line:
##        arr2.append(i)
##        if i not in arr:
##            arr.append(i)
    line=line.split(" ")
    for i in line:
        if len(i)>0:
            arrlen.append(len(i))
        if i!=u"" "and i not in arrlet":
            arrlet.append(i)
d={}
x=set(arrlet)
for i in x:
    d[i]=0
    for n in arrlet:
        if n==i:
            d[i]+=1
print len(arrlet)
print float(sum(arrlen))/len(arrlen)
##for i in arrlet:
##    d[i]=len(i)
for i in sorted(d, key=d.get, reverse=True):
    #print i, d[i]
    arr.append(d[i])
print sum(arr[0:1]+arr[3:11]+arr[14:23])/20
