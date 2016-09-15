# -*- coding: utf-8 -*-

import codecs, csv, lxml.etree


def gettags(filename):
    import re
    file = codecs.open(filename, 'r')
    f = file.read()
    file.close()
    tree = lxml.etree.fromstring(f)
    mass = tree.xpath("/corpora/*")
    return mass


def tablematerial(filename):
    mass = gettags(filename)
    arr = [[]]
    arr2 = [[]]
    for i in range(len(mass) - 1):
        arr.append([])
        if mass[i].tag == "no" and len(mass[i - 1].text) > 1 and len(mass[i + 1].text) > 1:
            minimass = [mass[i - 1].text[-2], mass[i - 1].text[-1], mass[i].text, mass[i + 1].text[0],
                        mass[i + 1].text[1], mass[i].get("right")]
            arr.append(minimass)
            minimass2 = [mass[i - 1].text[-2], mass[i - 1].text[-1], mass[i].get("right"), mass[i + 1].text[0],
                         mass[i + 1].text[1]]
            arr2.append(minimass2)
        if mass[i].tag == "yes" and len(mass[i].text) >= 5:
            for n in range(len(mass[i].text) - 4):
                arr2.append(list(mass[i].text[n:n + 5]))
    arr3 = []
    for i in arr:
        if i != []:
            arr3.append(i)
    arr2 = arr2[1:]
    for i in arr2:
        i.append(i[2])

    return arr3 + arr2


def makecsv():
    model = codecs.open("model.csv", 'w', 'utf-8')
    model.write("-2,-1,x,1,2,class\n")
    for i in tablematerial('dumdum.xml'):
        for n in i:
            model.write(",".join(n) + "\n")
    model.close()


def makemodel(arr=tablematerial("dumdum.xml")):
    import json
    mod = codecs.open('dummymodel.txt', 'w', 'utf-8')
    d={}
    for i in arr:
        mod.write(str(hash(i[-1])) + ' ' + '1:' + str(hash(i[0])) + ' 2:' + str(hash(i[1])) + ' 3:' + str(
            hash(i[2])) + ' 4:' + str(hash(i[3])) + ' 5:' + str(hash(i[4])) + '\n')
        for n in i:
            d[n]=hash(n)
    with open('hashdict.json', 'w') as jsfile:
        json.dump(d, jsfile)
    mod.close()


def main():
    from sklearn.datasets import load_svmlight_file
    from sklearn import svm
    from sklearn.externals import joblib
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    X_train, y_train = load_svmlight_file("dummymodel.txt")
    clf = svm.SVC()
    clf.fit(X_train, y_train)
    joblib.dump(clf, "dummy.pkl")


makemodel()
