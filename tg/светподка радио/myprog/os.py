#-*- coding:utf-8 -*-
import os
import codecs
import re
f = codecs.open('mir.htm', 'r', 'utf-8')
a = f.read()
part = re.split(u'\* ЧАСТЬ .*?\*', a)
i = 1
for onePart in part:
    if len(onePart)<36:
        continue
    #print 'chast!'
    part[i]  = re.split(u'[IVXLC]+?\.', onePart)
    i += 1
chast = 1
glava = 1
#print part[2][3]
for onePart in part:
    if len(onePart)<4:
        continue
    #print 'chast!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1'
    #print chast
    chast2 = str(chast)
    for oneChapt in onePart:
        if len(oneChapt) < 150:
            continue
        else:
            #print glava
            glava2 = str(glava)
            direct = u'Tom1\\' + chast2 + u'\\' + glava2 + u'\\'
            if os.path.exists(direct):
                  pass
            else:
                os.makedirs(direct)
            direct2 = direct + glava2 + u'.txt'
            w = codecs.open(direct2, 'w', 'utf-8')
            w.write(oneChapt)
            w.close()
            glava += 1
    glava = 1
    chast += 1
