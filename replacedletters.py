# -*- codecs: utf-8 -*-
import codecs, random, re

f=codecs.open("hearttransplant.txt", "r", "utf-8")

arrlet=[]
arrlen=[]
arr=[]
arr2=[]

for line in f:
    line=line.lower()
    line=re.sub(u"[—\.,!?\"»«…:]", "", line)
    line=re.sub(u"-", " ", line)
    for i in line:
        arr2.append(i)
        if i not in arr:
            arr.append(i)
    line=line.split(" ")
    for i in line:
        arrlen.append(len(i))
        for a in i:
            if a!=u"":
                arrlet.append(a)

a2=0
d={}
for i in arr:
    for n in arr2:
        if n==i:
            a2+=1
    d[i]=a2
    a2=0

for i in d:
    print i, u"-", float(d[i])/len(arr2)

arrtxt=[]

for i in range(len(arrlen)):
    x=random.choice(arrlen)
    a=u""
    for n in range(x):
        a+=random.choice(arrlet)
    arrtxt.append(a)

arrtxt=" ".join(arrtxt)
print arrtxt

print u"Полученный текст вообще не похож на оригинальный."

f.close()
