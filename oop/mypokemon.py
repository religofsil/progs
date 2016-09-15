import random


class Animal:
    def __init__(self):
        self.author = 'Sasha Ershova'

    def move(self, vicinity):
        return 'move', 4

    def give_birth(self):
        return 'newborn'

    def shouldigo(self, options):
        a = [0, 2, 7, 1, 8, 3, 6, 5, 4]
        random.shuffle(a)
        for i in a:
            if options[i][0] == 'food':
                return 'move', i
        for i in a:
            if options[i][0] != 'fence' and options[i][1] == None:
                return 'move', i
        for i in a:
            if i != 4 and options[i][0] != 'fence':
                return 'move', i


class Charmander(Animal):
    def __init__(self):
        self.name = 'Charmander'
        self.author = 'Sasha Ershova'
        self.speed = 0
        self.attack = 90
        self.color = u"#FF9966"
        self.marker = u'<'
        self.defense = 10

    def give_birth(self):
        newborn = Charmander()
        newborn = self.mutate(newborn)
        print newborn.speed, newborn.attack, newborn.defense
        return newborn

    def mutate(self, newborn):
        newborn.color = str(u'#' + random.choice((u'F', u'E', u'A', u'B', u'C')) * 2 + random.choice(
            (u'3', u'9', u'6', u'0')) * 2 + random.choice((u'3', u'9', u'6', u'0')) * 2)
        if self.attack < 100:
            a = random.choice((0, 1))
            if a == 0:
                if self.defense > 0:
                    newborn.attack = self.attack + 1
                    newborn.defense = self.defense - 1
            else:
                if self.speed > 0:
                    newborn.attack = self.attack + 1
                    newborn.speed = self.speed - 1
        return newborn

    def move(self, vicinity):
        a = [0, 2, 7, 1, 8, 3, 6, 5, 4]
        random.shuffle(a)
        options = []
        for i in vicinity:
            options.append(i)
        if vicinity[4][0] == 'food' and vicinity[4][1] == None:
            return 'eat', 4
        for n in a:
            if vicinity[n][0] == 'animal' and vicinity[n][1].name != 'Charmander':
                return 'attack', n
            else:
                pass
        try:
            return self.shouldigo(options)
        except:
            return 'move', 4
