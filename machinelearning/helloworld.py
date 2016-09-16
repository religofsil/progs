# -*- coding: utf-8 -*-
import codecs
def primary_cleaning(text):
    count=0
    cleaned_text=''
    for line in text:
        for i in line:
            if i in u'1234567890אבגדהוזחטיכךלמםנןסעפףצץקרשת ':
                count+=1
        print '---'
        print line
        print count
        print len(line)
        print float(count)/len(line)
        print '---'
        print ''
        if (float(count)/len(line))>0.2:
            cleaned_text=cleaned_text+line
        else:
            cleaned_text=cleaned_text+"------UNRECOGNISED LINE------\r\n"
        count=0
    return cleaned_text

f=codecs.open('test.txt', 'w', 'utf-8')
f.write(primary_cleaning(codecs.open('rawcorpora.txt', 'r', 'utf-8')))
f.close()
