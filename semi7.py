import codecs
f=codecs.open("C:\Python27\itwas.txt", "r", "utf-8")
i_s=0
vowels=[u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�", u"�"]
big_array=[]
syll_arr=[0]
for line in f:
    line=line.rstrip()
    i_s+=1
    vow=0
    words=line.split(" ")
    for word in words:
        l=vow
        for n in word:
             if n in vowels:
                 vow+=1
        if vow>l:
             big_array.append(vow)

print big_array
for a in big_array:
    i_a=0
    for b in big_array:
        if a==b:
            i_a+=1
    if i_a==i_s:
        if a not in serv_arr:
            syll_arr.append(a)
if len(syll_arr)=0:
    print u"���"
else:
    print syll_arr[1:]
