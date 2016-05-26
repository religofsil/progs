# -*- coding: utf-8 -*-
import codecs, json
slovar=codecs.open('slovar.json', 'r', 'utf-8')
slovar=json.load(slovar)
f=codecs.open('attributes.txt', 'w', 'utf-8')
arr=[]
for i in slovar:
    root=slovar[i]
    for n in root:
        root2=root[n]
        for x in root2[1]:
            if x not in arr:
                arr.append(x)
for i in arr:
    f.write(i+'\r\n')
f.close()