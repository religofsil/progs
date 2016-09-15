f = open('long_poem.txt', 'r', encoding='utf-8')
text = f.read()  # читаем текст
f.close()
text = text.split('\n')  # разбиваем текст на строки
search = input('к чему надо подобрать рифму?\n')

for i in text:
    lastword = i.split(' ')[-1]  # последнее слово в строке
    if lastword == search:  # ищем строки, в которых последнее слово -- то, которое мы ищем
        for n in range(-3, 3):  # смотрим от нужной строки на 3 вверх и на 3 вниз
            num = text.index(i) + n
            if text[num][-2:] == search[
                                 -2:]:  # если последние 2 символа строки совпадают с последними 2 символами запроса,
                print(text[num])  # то выводим строку
        print('')
