class data:
    def __init__(self, k, d):
        self.key = k
        self.d = d


class hashtab:
    hfunc = (5 ** 0.5 - 1) / 2

    def __init__(self, n):
        self.content = []
        for i in range(n):
            self.content.append(None)
        self.n = len(self.content)

    def add(self, x):
        key = int(((x.key * self.hfunc) % 1) * self.n)
        print key
        try:
            if self.content[key] is None:
                self.content[key] = x
                return 0
            else:
                if self.content[key].key == x.key and self.content[key].d == x.d:
                    return 1
                else:
                    self.add(None)
                    self.add(x)
                    return 0
        except:
            self.content[key] = x
            return 0

    def find(self, key):
        arrey = []
        for i in self.content:
            try:
                ey = int(((i.key * self.hfunc) % 1) * self.n)
                if self.content[ey].key == key:
                    return self.content[ey]
            except:
                pass
        return None

    def delete(self, key):
        arrey = []
        for i in self.content:
            try:
                ey = int(((i.key * self.hfunc) % 1) * self.n)
                if self.content[ey].key == key:
                    self.content[ey] = None
                    return 1
            except:
                pass
        return 0
