# -*- coding: utf-8 -*-

import re, codecs

file = codecs.open(u'C:/Users/Саша/Downloads/slovar1.txt', 'r', 'utf-8-sig')
text = file.read()
text = re.sub(u'-\r\n', u'', text)
text=re.sub(u'\r\n', u' ', text)
text=re.sub(u'  ', u' ', text)
file.close()
f2 = codecs.open('result.txt', 'w', 'utf-8-sig')
text=re.sub(u' (хА-Я)', text)

# f2 = codecs.open('result.txt', 'r', 'utf-8')
# text = f2.read()
# f2.close()
# text = re.sub(u'\r\n([А-Я][а-яё]+)\r\n', u'\1', text)
# text = re.sub(u'\r\n-', u'', text)
# f2 = codecs.open('result.txt', 'w', 'utf-8')
# f2.write(text)
# f2.close()
