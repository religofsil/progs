# -*- coding: utf-8 -*-
import random
n=0
arr=[u"привет!", u"нормально, ты как?", u":D", u"лол", u"", u":DDD", u"ахаха", u"бывает", u"эээ", u"ого", u"найс", u"прикольно", u"ничего", u"Ладно, мне надо дз делать. Спокойной!", u"спишемся)"]
for i in range(10):
    a=raw_input().decode("cp1251")
    a=a.lower()
    if u"привет" in a:
        print arr[0]
    elif u"как" in a and u"дела" in a:
        print arr[1]
    elif u"что" in a and "?" in a:
        print arr[12]
    elif u"пока" in a:
        print arr[-1]
        break
    else:
        print arr[random.randint(2,11)]
    n+=1
if n==10 and u"пока" not in a:
    print arr[13]
