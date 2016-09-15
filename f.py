import codecs
from flask import Flask, request, render_template
app=Flask(__name__)
##nam = {}
##a = codecs.open (u"names.csv", "r", "utf-8-sig")
##for line in a:
##    line = line.strip()
##    line = line.split(';')
##    nam[line[0]] = line[1]
forcsv=[]
@app.route('/form')
def form():
##    global nam
    i=0
    if len(request.args)>0:
        forcsv[i]=request.args['Name']
        i+=1
        forcsv[i]=request.args['Age']
        i+=1
        return u'<html><body>Hello,' + request.args['Name'] +u'!</body></html>'
    else:
        return render_template('example.html')
app.run(debug = True)
for i in forcsv:
    print i
        
    
