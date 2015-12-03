# -*- coding: utf-8 -*-
# Эля, прости, пожалуйста, за трудночитабельный код. Я исправлюсь!

import random

class Wug:
    color = u"#FF9966"
    marker = u'*'
    def __init__(self):
        self.name = u'wag'
        self.authors_name = u'Masza Szejanowa'
        self.speed = 0
        self.attack = 70
        self.defense = 30
        
    def move(self, vicinity):
        options = []
        for i in range(9):
            if vicinity[i][0] == u'animal' and vicinity[i][1].name!=u'wag':
                return u'attack', i
        for i in range(9):
            if vicinity[i][0] == u'desert' or vicinity[i][0] == 'food':
                options.append(i)

        ## информация о каждой клетке
        info = {}
        for i in range(9):
            info[i] = vicinity[i][0]

        ## чтобы была
        run_away = 42
        for i in range(9):
            if vicinity[i][0] == u'animal':
                if vicinity[i][1].attack > 40:

                    ## здесь я принимаю решение, куда бежать, если хочется
                    if (8 - i) in options:
                        run_away = 8 - i
                    elif (8 - i + 1) in options:
                        run_away = 8 - i + 1
                    elif (8 - i - 1) in options:
                        run_away = 8 - i - 1

        ## здесь я выбираю, что делать
        if vicinity[4][0] == 'food':
            action = 'eat'
        else:
            action = 'move'

        ## здесь я выбираю, куда идти
        place = self.where_go(run_away, options)
            
        return (action, place)

    def where_go(self, run_away, options):
        '''выбирает, на какую клетку идти'''
        if run_away != 42:
            place = run_away
        elif len(options) == 0:
            place = 4
        else:
            place = random.choice(options)
        return place

    def give_birth(self):
        '''возвращает нового себя'''
        new_one = Wug()
        new_one = self.skill_mutation(new_one)
        print str(new_one.defense), str(new_one.speed)
        return new_one

    def skill_mutation(self, baby):
        '''возвращает существо с изменёнными скилами'''
        decide = random.choice((1,0))
        if decide == 0:
            baby.defense = self.defense + 1
            baby.speed = self.speed - 1
        else:
            baby.defense = self.defense - 1
            baby.speed = self.speed + 1
        return baby