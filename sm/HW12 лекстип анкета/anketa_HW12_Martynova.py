# -*- coding: utf-8 -*-

import codecs
import re
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/form')
def index():
    try:
        global d
        lang = request.args['lang']
        pic1 = request.args['pic1']
        pic2 = request.args['pic2']
        w = codecs.open('fox.csv', 'a', 'utf-8')
        w.write(lang + u': ' + pic1 + u';' + lang + u': ' + pic2 + u'\r\n')
        w.close()
        return '<html><body><title>анкета!</title><p>спасибо!</p></body></html>'
    except:
        return render_template('form.html')
    
@app.route('/stats')
def stats():
##    d = {}
##    f = codecs.open('fox.csv', 'r', 'utf-8')
##    a = f.read()
##    f.close()
##    sent = a.split('\r\n')
    arr = []
    pic11 = []
    pic22 = []
    f = codecs.open('fox.csv', 'r', 'utf-8')
    for line in f:
        line = line.split(';')
        arr.append(line)
    for i in arr:
        pic11.append(i[0])
        pic22.append(i[1])
    return render_template('res.html', arr = arr, pic11 = pic11, pic22 = pic22)
app.run(debug = True)    
