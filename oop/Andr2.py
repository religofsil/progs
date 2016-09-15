# coding=utf-8
__author__ = 'Basilis'
import random

class Anim:
    def __init__(self):
        self.author = 'Bas'
        self.name = 'Animal'
        self.speed = 9
        self.attack = 81
        self.defense = 10

    def weight(self, recogn):
        """ суть в том, что присутствие опасного
            животного снижает вес окружающих его клеток"""
        for i in range(len(recogn)):
            if i in recogn:
                if recogn[i][0] == 'danger':
                    for n in range(9):
                        if 4 - i - n in recogn.keys:
                            recogn[4 - i - n][1] = float(recogn[4 - i - n][1]) - 0.5
        return recogn

    def fini(self, recogn):
        """ берутся все весы, из них выбирается максимальный, а потом из тех клеток,
          у которых максимальный вес, рандомно выбирается одна"""
        maxx = max([float(recogn[x][1]) for x in recogn])
        steps = [x for x in recogn if float(recogn[x][1]) == maxx]
        step = random.choice(steps)
        if step == 4 and recogn[4][0] == 'food':
            return 'eat', 4
        if recogn[step][0] == 'victim' or recogn[step][0] == 'danger':
            return 'attack', step
        if recogn[step][0] == 'desert' or recogn[step][0] == 'food':
            return 'move', step

    def give_birth(self):
        pass

    def move(self, vicinity):
        return ('move', 4)


# rhino = Anim()


# print rhino.move([('fence', None), ('fence', None), ('food', None), ('desert', None), ('food', None),\
#             ('food', None), ('desert', None), ('desert', None), ('desert', None)])

# food = 15 на каждом ходу снижается на 0,25
# a = Wug()
# a.food = 15  <- вот так просто берёшь и добавляешь свойство экземпляру класса
# p(A1) = A1.attack/(A1.attack+A2.defense+20)
# потом будет рекурсия муахаха
# решить проблему с атакой своего класса (бессмысленно и беспощадно)


class Rhino(Anim):
    def __init__(self):
        Anim.__init__(self)
        self.name = 'Rhino'
        self.speed = 9
        self.attack = 81
        self.defense = 10
        self.berserk = 71
        self.color = '#808080'
        self.marker = '*'

    def recognf(self, vicinity):
        recogn = {}
        for i in range(len(vicinity)):
            if vicinity[i][0] == 'animal' and vicinity[i][1].author == 'Bas':
                continue
            elif vicinity[i][0] == 'animal' and vicinity[i][1] > self.berserk:
                recogn[i] = ('danger', -0.5)
            elif vicinity[i][0] == 'animal' and vicinity[i][1] <= self.berserk:
                print vicinity[i][1].author
                recogn[i] = ('victim', 1)
            elif vicinity[i][0] == 'fence':
                continue
            elif vicinity[i][0] == 'desert':
                recogn[i] = ('desert', 0.5)
            elif vicinity[i][0] == 'food':
                recogn[i] = ('food', 0.8)
        return recogn

    def move(self, vicinity):
        c = Anim.fini(self, Anim.weight(self, self.recognf(vicinity)))
        return c

    def colouristics(self):
        c = int(self.color[1:])
        change = random.randint(-999999, 999999)
        result = c + change
        if len(str(abs(result))) >= 6:
            rescolour = '#' + str(abs(result))[:6]
        else:
            rescolour = '#' + str(100000 + abs(result))
        return rescolour


    def give_birth(self):
        rhino1 = Rhino()
        chars = ['attack', 'defense', 'speed']
        chars_mod = random.sample(chars, 2)
        if vars(rhino1)[chars_mod[0]] == 0:
            vars(rhino1)[chars_mod[0]] += 1
            vars(rhino1)[chars_mod[1]] -= 1
        else:
            vars(rhino1)[chars_mod[0]] -= 1
            vars(rhino1)[chars_mod[1]] += 1
        vars(rhino1)['berserk'] += random.choice([-1, 1])
        rhino1.color = self.colouristics()
        return rhino1

c = Rhino()
rhino1 = c.give_birth()
print vars(rhino1)