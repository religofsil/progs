import codecs
f=codecs.open("test.txt", "r", "utf-8-sig")
for line in f:
    line=line.rstrip()
text=" ".join(f)
print f
letters="qwertyuiopasdfghjklzxcvbnm"
for let in text:
    a=let.find(letters)
    a+=2
    print a
f.close()
