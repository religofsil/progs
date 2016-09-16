# -*- codecs: utf-8 -*-
import re, codecs, random
person=['je', 'tu', 'on', 'nous', 'vous', 'il', 'elle', 'ils', 'elles']
temp=['present simple', 'imparfait', 'passe compose', 'future simple', 'passe immediate', 'futur immediate', 'futur dans le passe', 'plus-que-parfait']

def inputter():
    arr=[]
    l=""
    while l!="stop":
        l=raw_input("input your infinitive: ")
        for i in person:
            for n in temp:
                a=l+'/'+n+'/'+i
                if l!='stop':
                    arr.append(a)
    try:
        f=codecs.open('frenchverbs.csv', 'a', 'utf-8')
    except:
        f=codecs.open('frenchverbs.csv', 'w', 'utf-8')
    for v in arr:
        print v
        f.write(v+"\t"+raw_input('type the correct form: ')+"\n")
        
inputter()
