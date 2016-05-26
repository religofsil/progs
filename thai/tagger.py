import os, nltk

def readfiles():
    arrwords = []
    for root2, dirs, files in os.walk('thai_dict'):
        for file in files:
            f = codecs.open(os.path.join(root2, file), "r", "utf-8")
            f = f.read()
            root = lxml.html.fromstring(f)
            words = root.xpath('//table[@class="gridtable"]/tr')
            words = words[1:-1]
            for i in words:
                arrwords.append(Word(i))
    print 'readdict finished'
    return arrwords