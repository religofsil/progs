# -*- coding: utf-8 -*-

import codecs
import re
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

f = codecs.open('text1.txt', 'r', 'utf-8')
a = f.read()
f.close()

@app.route('/')
def index():
    global a
    sent = a.split('\r\n')
    
    return render_template('res.html', sent = sent)
app.run(debug = True)    
