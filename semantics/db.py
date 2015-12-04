#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3, codecs

conn = sqlite3.connect('test.db')

c = conn.cursor() #создала точку соприкосновения с базой
#c.execute('''CREATE TABLE cat (id, text, year)''') #создали пустой лист с тремя колонками
table = codecs.open('tab.csv', 'r', 'utf-8')
for line in table:
    line = line.strip()
    idd, text, year = line.split(';')
    c.execute(u'''INSERT INTO cat VALUES (?, ?, ?)''', (idd, text, year))
conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

c = conn.cursor()
lines = [1,2]
for line in lines:
    c.execute(u'''SELECT text FROM cat WHERE id = ?''', (line,))
    text = c.fetchone() #а если много, то fetch
print text
