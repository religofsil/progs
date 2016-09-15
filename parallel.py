#!/usr/bin/python
# coding: utf-8
# Обрабатываем питоном TMX и вычисляем разницу в средних длинах предложений.

import sys
from xml.dom import minidom
import numpy as np
import scipy.stats as stats


#argument = sys.argv[1]

def extract_bitext(xml):
    # Парсим TMX и возвращаем словарь с предложениями и список языков
    doc = minidom.parse(xml)
    node = doc.documentElement
    translation_units = doc.getElementsByTagName("tu")
    languages = set()
    bitext_dic = []

    for tu in translation_units:
        tuvs = tu.getElementsByTagName("tuv")
        pairs = {}
        for tuv in tuvs:
            text = tuv.getElementsByTagName("seg")[0].childNodes[-1].data
            lang = tuv.getAttributeNode('xml:lang').nodeValue
            languages.add(lang)
            pairs[lang] = text
        bitext_dic.append(pairs)

    return (bitext_dic,languages)

# Загружаем файл в формате TMX
a = extract_bitext('words_en-words_ru.tmx')

sentence_lengths = []

for language in a[1]:
    # Для каждого языка собираем список длин предложений.
    lengths = []
    for i in a[0]:
        lengths.append(len(i[language]))
    sentence_lengths.append(lengths)
    print u'Средняя длина предложения для языка %s:' % language, np.average(lengths)

if len(sentence_lengths) == 2:
    # Вычисляем достоверность различий между наборами длин предложений по t-тесту. p - это вероятность того, что выборки всё же одинаковые.
    # Если больше 0.1 - мы не можем с уверенностью утверждать, что они различны.
    language1 = sentence_lengths[0]
    language2 = sentence_lengths[1]
    print u'Вероятность ошибки (P-значение) = %f' % stats.ttest_rel(language1, language2)[1]

