# -*- coding:utf-8 -*-
import codecs, json
from sklearn import svm
from sklearn.externals import joblib
from sklearn.datasets import load_svmlight_file


def reader(filename, model='dummy.pkl'):
    with open('hashdict.json') as jsfile:
        d = json.load(jsfile)
    d_inv = {v: k for k, v in d.items()}
    f = codecs.open(filename, 'r', 'utf-8')
    text = f.read()
    f.close()
    createfile(filename)
    clf = joblib.load(model)
    f = codecs.open('newcleancorp.txt', 'w', 'utf-8')
    f.write(text[0] + text[1])
    data, bogus = load_svmlight_file('data.txt')
    for i in data:
        expected = clf.predict(i)
        if expected[0] in d_inv:
            letter = d_inv[expected[0]]
        else:
            letter=d_inv[i]
        f.write(letter)
    f.write(text[-2] + text[-1])


def createfile(filename):
    f = codecs.open(filename, 'r', 'utf-8')
    text = f.read()
    f.close()
    arr = []
    with open('hashdict.json') as jsfile:
        d = json.load(jsfile)
    d_inv = {v: k for k, v in d.items()}
    for i in range(len(text) - 4):
        arr.append([d[n] for n in text[i:i + 5]])
    dataset = codecs.open('data.txt', 'w', 'utf-8')
    for i in arr:
        dataset.write('0 ' + '1:' + str(hash(i[0])) + ' 2:' + str(hash(i[1])) + ' 3:' + str(
            hash(i[2])) + ' 4:' + str(hash(i[3])) + ' 5:' + str(hash(i[4])) + '\n')


reader('rawishcorp.txt')
