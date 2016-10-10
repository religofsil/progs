import re, sqlite3, codecs

c = sqlite3.connect('freqdict.db')
cursor = c.cursor()
# c.execute("CREATE TABLE freqdict (word TEXT, frequency INTEGER)")
c.commit()


class Article:
    def __init__(self, xml='', title='', text='', links=[], valid=False):
        self.xml = xml
        self.title = title
        self.text = text
        self.links = links
        self.valid = valid


ttl = re.compile('<title>(.+?)</title>')
txt = re.compile('</?text>')
lnk = re.compile('\[\[(?:.+?\|)?(.+?)\]\]')
tagline = re.compile('</?.+?>')

table = codecs.open('tablewiki2.csv', 'w', 'utf-8')
table.write('title,links,words\n')

with open('dummywiki.xml', encoding='utf-8') as dump:
    count = 0
    art = Article()
    print('start')
    for line in dump:
        if '<article>' in line:
            if art.valid:
                table.write(art.title + ',' + str(len(art.links)) + ',' + str(len(art.text.split(' '))) + '\n')
                for i in art.text.split(' '):
                    try:
                        cursor.execute("SELECT frequency FROM freqdict WHERE word='%s'" % i)
                        val = cursor.fetchone()[0]
                        cursor.execute("UPDATE freqdict SET frequency=? WHERE word=?", (val + 1, i))
                        c.commit()
                    except:
                        cursor.execute("INSERT INTO freqdict VALUES (?,?)", (i, 1))
            art = Article()
        elif '<title>' in line:
            art.title = ttl.findall(line)[0]
            if ':' not in art.title:
                art.valid = True
        elif tagline.match(line):
            pass
        else:
            art.text = art.text + txt.sub('', line)
        art.links = lnk.findall(art.text)

table.close()

c.commit()
c.close()
