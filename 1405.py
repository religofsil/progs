# -*- coding: utf-8 -*-

import codecs
import re

def onegin(s):
    s2=re.sub (u"Базаров", u"Онегин", s)
    return s2

def eugine(s):
    s2=re.sub (u"(Евгени(.{,2}?)) Василье?в?ич", u"\\1", s)
    return s2

def peter(s):
    s2=re.sub (u"Паве?л(.{,2}?) Петрович(.{,2}?)", u"Родион\\1 Романович\\2", s)
    return s2

def akak(s):
    s2=re.sub (u"Никола(.{,2}?) Петрович(.{,2}?)", u"Акаки\\1 Акакиевич\\2", s)
    return s2

def bash(s):
    s2=re.sub ("(Акаки(.{,2}?) Акакиевич(.{,2}?)) Кирсанов", u"\\1 Башмачкин", s)
    return s2

def rask(s):
    s2=re.sub ("(Родион(.{,2}?) Романович(.{,2}?)) Кирсанов", u"\\1 Раскольников", s)
    return s2

def postmodern():
    f=codecs.open("dadsandkids.txt", "r", "utf-8")
    a=f.read()
    a=onegin(a)
    a2=eugine(a)
    a3=peter(a2)
    a4=akak(a3)
    a5=bash(a4)
    a6=rask(a5)
    print a6

postmodern()
