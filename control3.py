# -*- coding: utf-8 -*-

import codecs
import json
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/form')
def form():
    global a
    f=codecs.open('couzdra.json', 'r', 'utf-8-sig')
    s=json.load(f)
    lang=request.args['lang']
    if s[lang] in s:
        a=s[lang]
    else:
        a=u"Глокая куздра непереводима!"
    return render_template('couzdra.html')

@app.route('/couzdra')
def couzdra():
    return render_template('couzdra.html')

app.run(debug=True)
