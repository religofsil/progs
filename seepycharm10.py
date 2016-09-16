import codecs
from flask import Flask, request, render_template
app=Flask(__name__)
forcsv=[]
@app.route('/form')
def form():
    global forcsv
    i=0
    l=0
    if len(request.args)>0:
        forcsv[i]=request.args['Name']
        i+=1
        forcsv[i]=request.args['Age']
        i+=1
        f2=codecs.open(u"datas"+str(l)+".csv", "w", "utf-8")
        l+=1
        f2.write(forcsv[i-2]+";"+forcsv[i-1]+";")
        f2.close()
        return u'<html><body>Hello,'+request.args['Name']+u'!</body></html>'
    else:
        return render_template('form.html')
app.run(debug = True)

forcsv2=forcsv[1::2]
for i in forcsv2:
    i=int(i)
x=sum(forcsv2)/len(forcsv2)

@app.route('/stats')
def stats():
    global x
    return u'<html><body>Average age:'+x+u'</body></html>'
app.run(debug = True)
