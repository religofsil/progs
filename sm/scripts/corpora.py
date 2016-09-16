# -*- coding: utf-8 -*-

import codecs
import re
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

f = codecs.open('text1.txt', 'r', 'utf-8')
a = f.read()
arr_sent = re.findall(u'[.:?!"-] +?([А-ЯЁ].*?[.?!-]) +?[А-ЯЁ]', a, flags=re.U)
f.close()

@app.route('/')
def index():
    try:
        arr_res = []
        word = request.args['word']
        global arr_sent
        for i in arr_sent:
            spisok_slov = i.split(' ')
            if word in spisok_slov:
                arr_res.append(spisok_slov)
        return render_template('res.html', arr_res = arr_res, word = word)
    except:
        return render_template('form.html')
    
app.run(debug = True)    
