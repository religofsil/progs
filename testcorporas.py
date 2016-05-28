# -*-coding:utf-8 -*-
import codecs, lxml.etree

def gettags(filename):
    import re
    file = codecs.open(filename, 'r')
    f = file.read()
    file.close()
    tree = lxml.etree.fromstring(f)
    mass = tree.xpath("/corpora/*")
    return mass

def writeacorp(filename, clean=True):
    arr=gettags("dumdum.xml")
    f=codecs.open(filename, 'w', 'utf-8')
    if clean:
        for n in arr:
            if n.tag=='yes':
                f.write(n.text)
            if n.tag=='no':
                f.write(n.get('right'))
    else:
        for n in arr:
            f.write(n.text)
    f.close()

writeacorp('rawishcorp.txt', clean=False)
writeacorp('cleanishcorp.txt', clean=True)