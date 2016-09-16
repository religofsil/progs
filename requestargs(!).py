from flask import Flask, request, render_template
app=Flask(__name__)

arr=[]

@app.route('/quizresults')
def quizresults():
    global arr
    if request.args['Native']!='':
        arr.append(request.args['Native'])
    if request.args['Fork']!='':
        arr.append(request.args['Fork'])
    if request.args['Knife']!='':
        arr.append(request.args['Knife'])
    if request.args['Spoon']!='':
        arr.append(request.args['Spoon'])
    return render_template('/quizresults.html')
@app.route('/quiz')

def quiz():
    global arr
    return render_template('/quiz.html')
app.run(debug = True)

f=codecs.open("file.csv", "w", "utf-8")
for i in arr:
    f.write(i+";")
f.close()
