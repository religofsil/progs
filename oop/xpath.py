## -*- coding: utf-8 -*-

import lxml.etree


# Получаем узел по пути к нему

some_xml = "<foo><bar>Hi</bar></foo>"
tree = lxml.etree.fromstring(some_xml)
results = tree.xpath('/foo/bar')
for node in results:
    print node.tag, node.text
print '------------'
print


# Несколько узлов с одинаковым путем

some_xml = """
<foo>
    <bar>first</bar>
    <bar>sedond</bar>
</foo>
"""
tree = lxml.etree.fromstring(some_xml)
results = tree.xpath('/foo/bar')
for node in results:
    print node.tag, node.text
print '------------'
print


# Более глубокий путь

some_xml = """
<book>
    <chapter>
        <section>Some text</section>
    </chapter>
    <chapter>
        <section>
            <a>Some link</a>
        </section>
    </chapter>
    <chapter></chapter>
</book>
"""
tree = lxml.etree.fromstring(some_xml)
results = tree.xpath('/book/chapter/section')
for node in results:
    print node.tag, node.text
print '------------'
print


# Более глубокий путь (2)

some_xml = """
<book>
    <chapter>
        <section>Some text</section>
    </chapter>
    <chapter>
        <section>
            <a>Some link</a>
        </section>
    </chapter>
    <chapter></chapter>
</book>
"""
tree = lxml.etree.fromstring(some_xml)
results = tree.xpath('/book/chapter/section/a')
for node in results:
    print node.tag, node.text
print '------------'
print


# Более глубокий путь

some_xml = """
<book>
    <chapter>
        <section>Some text</section>
    </chapter>
    <chapter>
        <section>
            <a>Some link</a>
        </section>
    </chapter>
    <chapter></chapter>
    <a>Out-of-chapter link</a>
</book>
"""
tree = lxml.etree.fromstring(some_xml)
results = tree.xpath('//a')
for node in results:
    print node.tag, node.text
print '------------'
print


# Более глубокий путь

some_xml = """
<book>
    <chapter>
        <section>Some text</section>
    </chapter>
    <chapter>
        <section>
            <a>Some link</a>
        </section>
    </chapter>
    <chapter></chapter>
    <a>Out-of-chapter link</a>
</book>
"""
tree = lxml.etree.fromstring(some_xml)
results = tree.xpath('//section/a')
for node in results:
    print node.tag, node.text
print '------------'
print


# Использование атрибутов

some_xml = """
<xml>
    <div class="a">first</div>
    <div class="b">second</div>
    <div class="c">third</div>
</xml>
"""
tree = lxml.etree.fromstring(some_xml)
results = tree.xpath('/xml/div[@class="b"]')
for node in results:
    print node.tag, node.text
print '------------'
print

with open('books.xml') as f:
    some_xml=f.read()
tree=lxml.etree.fromstring(some_xml)
print len(tree.xpath('/catalog/book'))
print '------------'
print
for i in tree.xpath('//title'):
    print i.text
print '------------'
print
for i in tree.xpath('/catalog/book[@id="bk103"]/price'):
    print i.text