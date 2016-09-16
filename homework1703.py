# -*- coding: utf-8 -*-

import codecs
znaki=[u".", u",", u"(", u")", u":", u";", u"!", u"?"]
d={u"наш":0, u"нашего":0, u"нашему":0, u"нашим":0, u"нашем":0, u"наша":0, u'нашей':0, u"нашу":0, u"наше":0, u"нашему":0, u'наши':0, u"нашими":0, u"наших":0}
f=codecs.open("hearttransplant.txt", 'r', 'utf-8')
countall=0
for line in f:
    line=line.rstrip()
    line=line.lower()
    words=line.split(" ")
    for word in words:
        for z in znaki:
            word=word.replace(z, u"")
    for i in d:
        for word in words:
            if i==word:
                d[i]+=1
                countall+=1
print u"Количество словоформ:", countall
fem=d[u"наша"]+d[u"нашей"]+d[u"нашу"]
plur1=d[u"наши"]+d[u"наших"]+d[u"нашими"]
plur2=d[u"наши"]+d[u"наших"]+d[u"нашими"]+d[u"нашим"]
if plur1>fem:
    print u"Форм множественного числа больше"
elif plur2>fem:
    print u"Неизвестно"
else:
    print u"Форм женского рода единственного числа больше"
