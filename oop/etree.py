# -*- coding: utf-8 -*-


import lxml.etree


# Парсим XML, смотрим имя тэга и его содержимое

some_xml = "<root>data</root>"
root = lxml.etree.fromstring(some_xml)
print "XML:", some_xml
print "Tag name:", root.tag
print "Tag content:", root.text
print '---'


# Смотрим имя тэга и его содержимое для потомков

some_xml = "<root>data<child>child data</child></root>"
root = lxml.etree.fromstring(some_xml)
print "XML:", some_xml
print "Tag name:", root.tag
print "Tag content:", root.text
print "Child Tag name:", root[0].tag
print "Child Tag content:", root[0].text
print '---'


# Перебираем всех потомков тэга

some_xml = "<root><child1></child1><child2></child2><child3></child3></root>"
root = lxml.etree.fromstring(some_xml)
print "XML:", some_xml
print "Root tag name:", root.tag
print "Children:"
for child in root:
    print child.tag
print '---'


# Смотрим атрибуты тэга (существующие и нет)

some_xml = '<root interesting="totally"></root>'
root = lxml.etree.fromstring(some_xml)
print "XML:", some_xml
print "Root tag name:", root.tag
print "Root 'interesting' atribute:", root.get('interesting')
print "Root 'hello' attribute:", root.get('hello')
print '---'


# Поиск тэгов

some_xml = '<root><cat>Bob</cat><dog>Alice</dog><cat>Caroline</cat></root>'
root = lxml.etree.fromstring(some_xml)
print "XML:", some_xml
print "Root tag name:", root.tag
print "Cats names:"
for cat in root.findall('cat'):
    print cat.text
print '---'

