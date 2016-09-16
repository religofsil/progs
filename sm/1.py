# -*- coding: utf-8 -*-
import codecs
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

arr = []
arr1 = []
n = 0

        
@app.route('/form')
def index():
    try:
        login = request.args['login']
        year = request.args['year']
        global arr
        arr.append(year)
        w = codecs.open('fox.csv', 'a', 'utf-8')
        w.write(login + u';' + year + u';')
        w.close()
        return '<html><body><title>Hallo, Welt!</title><p>thank you</p></body></html>'
    except:
        return render_template('1.html')
    

@app.route('/stats')
def stats():
    global arr
    global n
    age = []
    for i in arr:
        p = 2014 - int(i)
        age.append(p)
    
    for j in age:
        n += j
    res = n / len(age)
    
    return '<html><body><title>Hallo, Welt!</title><p>Средний возраст всех заполнивших анкету: ' + str(res) + '</p></body></html>' 
app.run(debug = True)
