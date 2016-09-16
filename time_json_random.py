# -*- codecs: cp1251 -*-

import codecs, time, random

def counttime(arr1, count):
    t1=time.clock()
    for i in range(1000):
        if random.randint(1, count) in arr1:
            continue
    t2=time.clock()
    dif=(t2-t1)/count
    return dif

##arr1=[random.randint(1,500)*2 for i in range(1001)]
##arr2=[random.randint(1,50000)*2 for i in range(100001)]
##arr3=[random.randint(1,500000)*2 for i in range(1000001)]
##
##print counttime(arr1, 1000)
##print counttime(set(arr1), 1000)
##print counttime(arr2, 100000)
##print counttime(set(arr2), 100000)
##print counttime(arr3, 1000000)
##print counttime(set(arr3), 1000000)

f=codecs.open("davinciscode.json", "r", "utf-8-sig")
s=json.load(f)
f.close()
f2=codecs.open("hearttransplant.txt", "r", "utf-8")
for line in f2:
    for i in range(len(line)):
