#-*- coding:cp1251 -*-
import codecs
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
csv = ''
ave = []
def voz(point):
    if len(point) == 4:
        point = 2014 - int(point)
    elif len(point) == 2:
        point = 114 - int(point)
    else:
        point = ''
    return point
@app.route('/form')
def index():
    global csv
    global ave
    if len(request.args)>0:
        csv += request.args['name'] + ';' + request.args['age'] + '\r\n'
        ave.append(request.args['age'])
        s = codecs.open('output.csv', 'w', 'cp1251')
        s.write(csv)
        return render_template('form.html')
    else:
        return render_template('form.html')
@app.route('/stats')
def index2():
    global ave
    i = 0
    su = 0
    page = u'<html><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> Средний возраст - '
    for point in ave:
        if voz(point) != '':
            su += int(voz(point))
            i += 1
    if i == 0:
        page += u'no!!!!!!'
    else:
        know = su/i
        page += str(know)
##        inf = u'всего человек   ' + str(i) + u', всего лет   ' + str(su) 
##        page += inf
    return(page)
app.run(debug = True)

