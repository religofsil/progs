import codecs, json

def writedict(arr):
    import json
    f = codecs.open('slovar2.json', 'w', 'utf-8')
    d = {}
    print 'starting with dict'
    for i in arr:
        d[i.thaiword]={}
    print 'i made an empty dict'
    for i in d:
        for n in arr:
            d[n.thaiword][count]=[n.translation, n.pos, n.translit]
            count+=1
            print n.thaiword, d[n.thaiword]
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.close()

class Word:
    def __init__(self, thaiword, translation, pos, translit):
        self.thaiword=thaiword
        self.translation=translation
        self.pos=pos
        self.translit=translit

word1=Word("THAIWORD", 'TRANSLATION', 'POS', 'TRANSLIT')
word2=Word("THAIWORD2", 'TRANSLATION2', 'POS2', 'TRANSLIT2')
word3=Word("THAIWORD", 'TRANSLATION3', 'POS3', 'TRANSLIT3')

writedict([word1, word2, word3])