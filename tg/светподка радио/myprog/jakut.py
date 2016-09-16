#-*- coding:utf-8 -*-
import codecs
import os
import re
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
path = u'myprog'
def clearing(a):
    a = a.replace(u'<', u'&lt;')
    a = a.replace(u'<', u'gt;')
    a = a.replace(u'\r\n',u'<br>')
    a = a.replace(u' ',u'&nbsp')
    a = re.sub(u'(".*?")', u'<i>\\1</i>', a, flags = re.U)
    a = re.sub(u"('.*?')", u'<i>\\1</i>', a, flags = re.U)
    a = re.sub(u'(import|for|(:?in )|else|while|continue|break|from|def|pass|return|True|False|import|if|elif|print|=|\+|\(|\\|\)|\[|\]|\))', u'<font color = "blue"><b>\\1</b></font>', a, flags = re.U)
    a = re.sub(u'(#.+?<br>)', u'<font color = "green">\\1</font>', a, flags = re.U)
    a = re.sub(u'(#.*?)(<font color = "blue"><b>)(.+?)(</b></font>)(.*?<br>)', u'\\1\\3\\5', a, flags = re.U)
    a = re.sub(u'(".*?)(<font color = "blue"><i>)(.+?)(</i></font>)(.*?<br>)', u'\\1\\3\\5', a, flags = re.U)
    a = re.sub(u'(\'.*?)(<font color = "blue"><i>)(.+?)(</i></font>)(.*?<br>)', u'\\1\\3\\5', a, flags = re.U)
    a = u'<html><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">' + a + u'</html>'
    # a = a.replace(u'coding',u'<br>')
    return a
x = os.listdir(path)
@app.route('/')
def index():
    global x
    if request.args:
        a = request.args['point']
        way = u'myprog/' + a 
        f = codecs.open(way, 'r', 'cp1251')
        a = f.read()
        b = clearing(a)
        f.close()
        return b
    else:
        return render_template('form.html', x=x)
app.run(debug = True)
 
