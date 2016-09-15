import os
import re
import codecs
a=os.listdir('.')
b=[]
for root, dirs, files in os.walk(u'.'):
    for i in files:
        i=re.split("\\....?.?", i)
        i=i[0]
        if i not in b:
            b.append(i)
s=len(b)
print s
