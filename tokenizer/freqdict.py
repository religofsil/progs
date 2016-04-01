# -*- coding:utf-8 -*-
import re, codecs
from collections import Counter

arr = []
except_arr = []
clean_text = codecs.open('cleancorpora.txt', 'w', 'utf-8-sig')


def readex():
    """открывает файл с регулярками и компилит их в регэксп"""
    f = codecs.open('exceptions.txt', 'r', 'utf-8')
    excep = []
    for line in f:
        excep.append(re.compile(line.strip(u'\n')))
    f.close()
    return excep


def treat(exceptions, line=''):
    """всё делается методом найти-и-обезвредить"""
    global except_arr  # arr - массив со всеми токенами
    for i in exceptions:
        for n in re.findall(i, line):
            print n
            except_arr.append(n.strip())
        line = re.sub(i, ' ', line)
        line = re.sub(u'  ', ' ', line)
        line = line.replace(u'…', ' ')
        line = line.replace(u' ', ' ')
    return line


def linetreat(line, exceptions):
    """потерявшую все исключения строку чистят от знаков препинания
    и создают разрезанную по пробелам копию"""
    line = treat(exceptions, line)
    clean_text.write(line)
    line = line.lower()
    line = line.rstrip()
    line = re.sub(u'[?!.”«»“,_;:—"()\[\]]', u' ', line)
    line = re.sub(u'  ', ' ', line)
    line = line.split(' ')
    return line


def makedict(arr):
    """частотный словарь"""
    d = Counter(arr)
    f = codecs.open('testfreqdict.txt', 'w', 'utf-8')
    for n in sorted(d, key=d.get, reverse=True):
        f.write(n + ' : ' + str(d[n]) + '\r\n')
    f.close()


def sentence_splitter(text):
    '''получает на вход целый текст, записывает по предложениям в отдельный файл, ничего не возвращает'''
    text = text.read()
    sentences = codecs.open('sentences.txt', 'w', 'utf-8-sig')
    reg = re.compile(u'(\\S\\S[.?!])[\n\s]')
    text = re.sub(u'\[.+?\]', '', text)
    text = reg.split(text)
    for i in text:
        if len(i) != 3:
            i = i.rstrip()
            sentences.write(i)
        else:
            i = i.rstrip()
            i += u'\0'.lstrip()
            i += u'\n'
            sentences.write(i)


def main():
    f = codecs.open('corpora.txt', 'r', 'utf-8')
    global arr
    global except_arr
    global clean_text
    exceptions = readex()
    for line in f:
        line = linetreat(line, exceptions)
        for i in line:
            if i != '':
                arr.append(i)
    f.close()
    clean_text.close()
    clean_text = codecs.open('cleancorpora.txt', 'r', 'utf-8-sig')
    sentence_splitter(clean_text)
    makedict(arr)


main()
