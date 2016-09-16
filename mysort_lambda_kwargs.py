import re
import codecs

def mysort(i=0):
    i=i.split(" ")
    return i[1]

arr1=['here today', 'now again', 'after midnight', 'since november']
arr=["here","now","after","since"]
arr1.sort(key=mysort)
print arr1

freqdict={"n":492, "e":5, "w":90}

for i in sorted(freqdict, key=lambda x:-freqdict[x]):
    print i

def myfunct(x, **kwargs):
    a=codecs.open(x, "r", "utf-8")
    for line in a:
        if "{{" in line and "}}" in line:
            line=re.sub("{{ *", "{{", line)
            line=re.sub(" *}}", "}}", line)
        for i in kwargs:
            if "{{"+i+"}}" in line:
                line=line.replace("{{"+i+"}}", kwargs[i])
        line=re.sub("{{[A-Za-z].*}}", "", line)
        print line

myfunct("shab.html", title="Klikukha", title2="imechko")
