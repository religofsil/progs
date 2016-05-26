# -*- coding: utf-8 -*-
import lxml.html, os, codecs


class Word:
    def __init__(self, root=None):
        try:
            self.thaiword = root.xpath('./td[@class="th"]')[0].text_content()
        except:
            self.thaiword = 'NO'
        try:
            self.pos = root.xpath('./td[@class="pos"]')[0].text_content().split(', ')
            if self.pos == ['']:
                self.pos = ["pos is missing"]
        except:
            self.pos = ["pos is missing"]
        if self.thaiword != 'NO':
            self.translit = root.xpath('./td')[1].text_content()
        else:
            self.translit = 'NO'
        try:
            self.translation = root.xpath('./td')[-1].text_content()
        except:
            self.translation = 'NO'

    def __gt__(self, other):
        return self.thaiword > other.thaiword

    def __lt__(self, other):
        return self.thaiword < other.thaiword

    def posmerge(self):
        changedict = {
            'ADJ': 'adjective',
            'adj': 'adjective',
            'N': 'noun',
            '์N': 'noun',
            '์์N': 'noun',
            'ืN': 'noun',
            'V': 'verb',
            '์V': 'verb',
            'VI': 'verb, intransitive',
            'VT': 'verb, transitive',
            'ADV': 'adverb',
            'AVD': 'adverb',
            'PRON': 'pronoun',
            'AUX': 'auxiliary verb',
            'IDM': 'idiom',
            'ABBR': 'abbreviation',
            'INT': 'interjection',
            'CONJ': 'conjunction',
            'CLAS': 'classifier',
            'PREP': 'preposition',
            'PREF': 'prefix',
            'ADV   V': 'adverb, verb'
        }
        for i in self.pos:
            if i in changedict:
                if i == 'VI' or i == 'VT':
                    self.pos.extend(changedict[i].split(', '))
                else:
                    self.pos.append(changedict[i])
                self.pos.remove(i)
        return self


def readdict():
    arrwords = []
    for root2, dirs, files in os.walk('thai_dict'):
        for file in files:
            f = codecs.open(os.path.join(root2, file), "r", "utf-8")
            f = f.read()
            root = lxml.html.fromstring(f)
            words = root.xpath('//table[@class="gridtable"]/tr')
            words = words[1:-1]
            for i in words:
                arrwords.append(Word(i).pos)
    return arrwords


def yaitron():
    import lxml.etree
    final_arr = []
    dict = codecs.open('yaitron.xml', 'r', 'utf-8')
    dict = dict.read()
    root = lxml.etree.fromstring(dict)
    words = root.xpath("//entry[@lang='tha']")
    for word in words:
        i = Word()
        i.pos = [word.xpath('./pos')[0].text]
        i.thaiword = word.xpath('./headword')[0].text
        i.translit = 'NO'
        i.translation = word.xpath('./translation')[0].text
        i = i.posmerge()
        final_arr.append(i.pos)
        i = None
    words = root.xpath("//entry[@lang='eng']")
    for word in words:
        i = Word()
        try:
            i.pos = word.xpath('./pos')[0].text.split(', ')
        except:
            i.pos = [""]
        i.translation = word.xpath('./headword')[0].text
        i.translit = 'NO'
        i.thaiword = word.xpath('./translation')[0].text
        i = i.posmerge()
        final_arr.append(i.pos)
        i = None
    return final_arr


def main():
    arr = readdict()
    arr.extend(yaitron())
    attr = codecs.open('attributes.txt', 'w', 'utf-8')
    trash=[]
    for i in arr:
        for n in i:
            if n not in trash:
                attr.write(n)
                attr.write('\r')
                trash.append(n)
    attr.close()


main()
