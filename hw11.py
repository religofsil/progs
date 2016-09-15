import codecs
import re
from flask import Flask, request, render_template
app=Flask(__name__)

def opening(name):
    f = codecs.open(name, 'r', 'utf-8')
    arr=[]
    for line in f:        
        line = line.rstrip()
        a = a.lower()        
        words = re.split('[.!?]', a)
        for i in words:
            if len(i)>0:
                arr.append(i)
    return arr

word=raw_input("enter some word")
a2=opening("text.txt")
mass=[]
arrst=[]
for i in a2:
    for l in i:
        if l==word:
            mass.append(i)
for i in mass:
    i=i.split(" ")
    for l in len(i):
        if i[l]==word:
            n1=" ".join(i[0:l-1])
            n2=" ".join(i[l+1:-1])
            arrst.append(n1)
            arrst.append(n2)

@app.route('/result')
def result():
    global word
    global arrst
    return render_template('search.html')
app.run(debug = True)
