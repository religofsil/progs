# -*- coding: utf-8 -*-
import re, codecs

PERSON_RE = re.compile(u'<div class="post person">.*?<div class="post person">', flags=re.S)
name=re.compile(u'title="(.+?)"')
phone=re.compile(u'<div class="l-extra small">(.*?)<br>')
email=re.compile(u'hseEObfuscator\(\n.+')
occupation=re.compile(u'<p class="with-indent7">.+?</p>')

def parse_blocks(html):
    pos = 0
    blocks = []
    while pos < len(html):
        res = PERSON_RE.search(html[pos:])
        if res is None:
            break
        pos += res.start() + 1
        blocks.append(res.group())
    return blocks


def main():
    with open('person-k.html') as f:
        html = f.read().decode('utf-8')
    blocks = parse_blocks(html)
    print len(blocks)
    print blocks[0]
    final_array=[]
    for i in blocks:
        final_array.append(i)

class Person:
    def __init__(self, string):
        self.person=string

def dismember(person):
        a=Person(person)
        a.name=name.search(person).group().split(' ')
        a.firstname=a.name[1]
        a.firstname=re.sub('"', '', a.firstname)
        a.lastname=a.name[0]
        a.lastname=re.sub('title="', '', a.lastname)
        if len(a.name)>2:
            a.fathername=a.name[2]
            a.fathername=re.sub('"', '', a.fathername)
        else:
            a.fathername=''
        try:
            a.phone=phone.search(person).group()
            a.phone=re.sub('<div class="l-extra small">', '', a.phone)
            a.phone=re.sub('<br>', '', a.phone)
        except:
            a.phone=''
        try:
            a.mails=email.search(person).group()
            a.mails=re.sub('hseEObfuscator\(\n', '', a.mails)
            a.mails=re.split('\],\[', a.mails)
            a.mail=a.mails[-1]
            a.mail=re.sub('\t|"|\[|\]|,', '', a.mail)
        except:
            a.mail=''
        try:
            a.occupation=occupation.search(person).group()
            a.occupation=re.sub('<br>', ', ', a.occupation)
            a.occupation=re.sub('<.+?>', '', a.occupation)
        except:
            a.occupation=''
        return a

main()
