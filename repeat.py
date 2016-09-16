словари
for word in a:
    if word in d:

d[word]+=1
for word in d:
    f.write(word+" "+str(d[word])+"\n")
d.sorted() -- сортировка
for words in sorted(d, key=d.get, reverse=True):
    f.write(word+" "+str(d[word])+"\n") -- вывод словаря, отсортированного по знач-ям в обратном порядке
