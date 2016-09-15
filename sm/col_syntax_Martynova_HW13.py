# -*- coding: utf-8 -*-

import codecs
import re
import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

x = os.listdir('scripts')

@app.route('/form')
def index():
    global x
    if request.args:
        a = request.args['point']
        name = 'scripts\\' + a
        f = codecs.open(name, 'r', 'utf-8')
        code = f.read()
        f.close()
        code = code.replace('\r\n', '\r\n<br>')
        code = code.replace(' ', '&nbsp')
        code1 = re.sub(u'((".*?")|(\'.*?\'))',u'<span style = "color:green">\\1</span>', code, flags=re.U)
        code2 = re.sub(u'(import|from|print|global|if|return|else|for|in|continue)&nbsp',u'<span style = "color:orange">\\1&nbsp</span>', code1, flags=re.U)
        code3 = re.sub(u'(try|except):',u'<span style = "color:orange">\\1</span><span style = "color:black">:</span>', code2, flags=re.U)
        code4 = re.sub(u'(#.*)',u'<span style = "color:red">\\1</span>', code3, flags=re.U)
        code5 = re.sub(u'(True|False)',u'<span style = "color:purple">\\1</span>', code4, flags=re.U)
        code6 = re.sub(u'(def&nbsp)(.*?)(\(\):)',u'<span style = "color:orange">\\1</span><span style = "color:blue">\\2</span><span style = "color:black">\\3</span>', code5, flags=re.U)
##        return render_template('res.html', code = code)
        return code6
    else:
        return render_template('form.html', x = x)
    
app.run(debug = True)
