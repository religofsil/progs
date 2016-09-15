# -*- coding: utf-8 -*-
import codecs, json, re

transitions = {
    'V': 'VB',
    't': 'VB',
    'i': 'VB',
    'N': 'NN',
    'h': 'NN',
    'A': 'JJ',
    'v': 'RB',
    'C': 'CC',
    'P': 'IN',
    '!': 'UH',
    'r': 'PRP',
    'D': 'DT',
    'I': 'DT'
}
final_dict = {}
dictionary = codecs.open('part-of-speech.txt', 'r', 'utf-8')
for word in dictionary:
    word = re.split('\t\|?', word)
    if word[1] in transitions:
        word[1] = transitions[word[1]]
    if word[1] not in final_dict:
        final_dict[word[1]] = []
    else:
        final_dict[word[1]].append(word[0])
print final_dict
f=codecs.open('pos.json', 'w', 'utf-8')
json.dump(f, final_dict)
f.close()
