f = open('long_poem.txt', 'r', encoding='utf-8')
text = f.read()
f.close()
text = text.split('\n')
search = input('к чему надо подобрать рифму?\n')

for i in text:
    lastword = i.split(' ')[-1]
    if lastword == search:
        for n in range(-3, 3):
            num = text.index(i) + n
            if text[num][-2:] == search[-2:]:
                print(text[num])
        print('')
