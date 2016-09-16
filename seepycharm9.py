# -*- coding: cp1251 -*-
import codecs
from flask import Flask
app = Flask(__name__)
from flask import request
from app import views
@app.route("/<page1>")
def index(page1):
    return u'<html><head><title>something</title></head><body><form><span><p>Имя: </p></span><input type="text" name="Name"><br /><span><p>Возраст: </p></span><input type="text" name="Age"><br /><input type="submit" name="submit"></body></html>'
app.run(debug=True)
