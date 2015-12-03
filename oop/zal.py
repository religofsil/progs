import codecs, copy

class Zaliznyak:
    def __init__(self, str):
        self.str = str

    def __lt__(self, other):
        i = -1
        try:
            while self.str[i] == other.str[i]:
                i -= 1
            else:
                return self.str[i] < other.str[i]

        except:
            return len(self.str) < len(other.str)

    def __eq__(self, other):
        return self.str == other.str

    def __ne__(self, other):
        return self.str != other.str

    def __gt__(self, other):
        return __lt__(self, other) == False and __eq__(self, other) == False

    def __ge__(self, other):
        return __lt__(self, other) == False

    def __le__(self, other):
        return __gt__(self, other) == False

    def __add__(self, other):
        return Zaliznyak(self.str + other.str)

    def __len__(self):
        return len(self.str)

    def __getitem__(self, item):  # item -- key or number
        return self.str[item]

    def __setitem__(self, key, value):
        self.str=self.str[:key]+value+self.str[key+1:]


class Text:
    def __init__(self, str):
        self.str = str
        self.words = len(self.str.split(' '))

    def __lt__(self, other):
        return self.words < other.words

    def __eq__(self, other):
        return self.words == other.words

    def __ne__(self, other):
        return self.words != other.words

    def __gt__(self, other):
        return __lt__(self, other) == False and __eq__(self, other) == False

    def __ge__(self, other):
        return __lt__(self, other) == False

    def __le__(self, other):
        return __gt__(self, other) == False

class Freqdict:
    def __init__(self, str=''):
        self.d={}
        if str!='':
            for i in str:
                if i not in self.d:
                    self.d[i]=1
                else:
                    self.d[i]+=1

        for i in self.d.keys():
            self.i=self.d[i]

    def __len__(self):
        return len(self.d.keys())

    def __getitem__(self, item):
        return self.i

    def __setitem__(self, key, value):
        self.i=value

    def __add__(self, other):
        dsum={}
        for i in self.d:
            if i in other.d:
                dsum[i]=self.i+other.i
            else:
                dsum[i]=self.i
        for i in other.d:
            if i in dsum:
                pass
            else:
                dsum[i]=other.i
        x=Freqdict()
        Freqdict.d=dsum
        return x

f1=Freqdict('abcab')
print f1['a'] #2
f1['b']=3
print len(f1) #3

f2=Freqdict('xyzc')
f3=f1+f2
print f3['c'] #2
print f3['b'] #3

a = Zaliznyak('tree')
b = Zaliznyak('tea')
c = Zaliznyak('teatree')
d = Zaliznyak('tree')
arr = [a, b, c, d]
print [i.str for i in sorted(arr)]
e = a + b
print e[1]
e[1]='0'
print e.str

f = Text('fcgvh io erf')
e = Text('dfgd g')
z = Text('zsdf')
arr2 = [f, e, z]
print [i.str for i in sorted(arr2)]
