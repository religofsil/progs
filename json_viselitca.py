# -*- codecs: utf-8 -*-

import json, codecs, copy

x=u'петя'
l=len(x)+1
stars=u"*"*len(x)
print stars
arr=[]
chkd=[]
while len(chkd)<=len(x)+1:
    d={}
    if stars==x:
        print u"Вы выиграли!"
        break
    let=raw_input(u"Введите букву: ").decode("cp1251")
    if let=="BACK":
        d=arr[-2]
        chkd.pop()
        d2=copy.deepcopy(d)
        arr.append(d2)
        print d[u'guessed_part']
        continue
    elif let in chkd:
        print u"Такая буква уже была!"
        continue
    else:
        d[u'current_letter']=let
        chkd.append(let)
        d[u'checked_letters']=chkd
        if let in x:
            for w in range(len(x)):
                if x[w]==let:
                    stars=stars[0:w]+let+stars[w+1:]
            d[u'guessed_part']=stars
            print stars
        else:
            print u"Нет такой буквы в этом слове!"
        d2=copy.deepcopy(d)
        arr.append(d2)
if stars!=x:
    print u"Вы проиграли!"

f=codecs.open("execution.json", "w", "utf-8")
json.dump(arr, f, ensure_ascii=False, indent=2)
f.close()
