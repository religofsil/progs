# -*- coding: utf-8 -*-
from flask import Flask #певый - название модуля, второй - название штуки, чтобы не писать каждый раз flask.import

##i = 0
app = Flask(__name__)
##@app.route('/')
##def index():
##    global i
##    i += 1
##    return u'<html><body><p>Hello world!\n' + str(i) + '</p></body></html>' 
##app.run(debug = True)
#127.0.0.1:5000 - 5000 это порт, на котором живет программа

d = {}
@app.route('/<username>')
def index(username):
    global d #переносит d в функцию
    if username not in d:
        d[username] = 1
    else:
        d[username] += 1 
    return u'<html><body><p>Welcome, ' + username + ' ' + str(d[username]) + '\n</p></body></html>'
    

app.run(debug = True)

##get -- передача параметров через адрес
##после ? -- параметры (а=с, а -- имя, с -- знач-е)
##<input type="text" name="login">(ввод текста)
##<input type="submit"> -- кнопка отправки
templates
