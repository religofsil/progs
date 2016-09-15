# -*- coding: utf-8 -*-


class OldString:
    def __init__(self, text):
        self.alphabet = u'абвгдежзиiклмнопрстуфхцчшщъыьѣэюяѳѵ'
        self.d = {}
        for i in self.alphabet:
            self.d[i] = self.alphabet.index(i)
        self.text = text.lower()

    def __lt__(self, other):
        i = 0
        try:
            while self.text[i] == other.text[i]:
                i += 1
            else:
                return self.d[self.text[i]] < other.d[other.text[i]]

        except:
            return len(self.text) < len(other.text)

    def __eq__(self, other):
        return self.text == other.text

    def __ne__(self, other):
        return self.text != other.text

    def __gt__(self, other):
        return __lt__(self, other) == False and __eq__(self, other) == False

    def __ge__(self, other):
        return __lt__(self, other) == False

    def __le__(self, other):
        return __gt__(self, other) == False


s1 = OldString(u'бѣлый')  # или сначала s1 = OldString(), а потом, например, s1.text = u'бѣлый'
s2 = OldString(u'бебебе')
s3 = OldString(u'Ѳедоръ')
array = [s1, s2, s3]
for s in sorted(array):
    print s.text  # слова должны распечататься в алфавитном порядке
