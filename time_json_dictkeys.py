# -*- codecs: utf-8 -*-
import time, json, codecs

def howlong(func):
    t=0
    for i in range(100):
        t1=time.clock()
        func
        t2=time.clock()
        t=t+(t2-t1)
    t=t/100
    return u"время работы функции: "+str(t)
    
    
f=codecs.open("kart.json", "r", "utf-8-sig")
s=json.load(f)
f.close()

def gruz(x, x2):
    n=dict.keys(x2)
    f2=codecs.open(x, "r", "utf-8")
    f3=codecs.open("transliteration.txt", "w", "utf-8")
    for line in f2:
        for i in range(len(line)):
            if line[i] in n:
                o=n.index(line[i])
                line=line[0:i]+s[n[o]]+line[i+1:]
        f3.write(line)
    f2.close()
    f3.close()

print u"для текста в 1000 символов "+howlong(gruz("gruz1000.txt", s))
print u"для текста в 100000 символов "+howlong(gruz("gruz100000.txt", s))
print u"для текста в 1000000 символов "+howlong(gruz("gruz1000000.txt", s))
