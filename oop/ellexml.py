import lxml.etree, lxml.html
some_xml='<no><nope mode="off">go to hell</nope></no>'
root=lxml.etree.fromstring(some_xml)
print 'root tag name: ', root.tag
print 'child tag name: ', root[0].tag
print 'say whaaat? ', root[0].text
