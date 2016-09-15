# -*- codecs: utf-8 -*-

import copy
import codecs
import re

def sumall (*args):
    i=0
    for l in args:
        i+=l
    return i

print sumall(6,5,456,9,2,12)

def findngramms (f, n, *args):
    f=codecs.open(f, "r", "utf-8")
    for line in f:
        line=line.lower()
        line=re.sub("[,.\—]", "", line)
        line=line.split(" ")
        arr=[]
        for l in line:
            l2=copy.deepcopy(l)
            for i in range(n):
                try:
                    l2=l2+" "+line[line.index(l)+i+1]
                except:
                    pass
                if len(l2.split(" "))==n:
                    arr.append(l2)
                    #print l2
    for i in arr:
        print i
##    for i in args:
##        for x in arr:
##            if i==x:
##                print x

                
##            for i in args:
##                if i in l:
##                    arr=[]
##                    arr2=[]
##                    for i in range (n):
##                        a=line.index(l)+1-n
##                        for i in range(n):
##                            try:
##                                arr.append(line[a])
##                            except:
##                                continue
##                            a+=1
##                        if len(arr)==n:
##                            arr=" ".join(arr)
##                            print arr
##                        a+=1
                        
findngramms("hearttransplant.txt", 3, u"что", u"любовь")
