#-*- coding: utf-8 -*-
import codecs
import re
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
def res():
    res = []
    for i in range(0,8):
        # print i
        res.append({})
        f = codecs.open('output.csv', 'r', 'cp1251')
        for line in f:
           # print 'going'
            line = line.split(';')
            if line[0] in res[i]:
              #  print 'if'
                res[i][line[0]] = res[i][line[0]] + ', ' + line[i+1]
            else:
              #  print 'else'
                res[i][line[0]] = line[i+1]
       # print res[i]
    for i in res:
        for j in i:
            text = ''
            for l in j:
                text = text + l
            j = text
    return res
@app.route('/')
def index():
    if len(request.args)>0:
        csv = request.args['ling'] + u';' + request.args['qu1'] + u';' + request.args['qu2'] + u';' + request.args['qu3'] + u';' + request.args['qu4'] + u';' + request.args['qu5'] + u';' + request.args['qu6'] + u';' + request.args['qu7'] + u';' + request.args['qu8'] + u'\r\n'
        s = codecs.open('output.csv', 'a', 'cp1251')
        s.write(csv)
    return render_template('form.html')
@app.route('/stats')
def index2():
    return render_template('stats.html', res0=res()[0], res1=res()[1], res2=res()[2], res3=res()[3], res4=res()[4], res5=res()[5], res6=res()[6], res7=res()[7])
app.run(debug = True)
 
 

