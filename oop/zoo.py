import random, time, os, re
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.lines import Line2D

def ddistr(probabilities):
    cdf = [(i, sum(p for j,p in probabilities if j < i))\
           for i,_ in probabilities]
    r = random.random()
    return max(i for i,c in cdf if c <= r)

class Zoo:
    def __init__(self):
        self.width = 30
        self.area = [[(ddistr([('food', 0.1), ('desert', 0.9)]), None)\
                      for i in range(self.width)] for j in range(self.width)]
        self.animals = {}   # {'animal': animal, 'x': x, 'y': y,
                            # 'move': (action, direction)}
        self.battles = []
        self.messages = []
        self.nTurn = 0

    def start(self):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, self.width), ylim=(0, self.width))
        self.zooPlot = []
        anim = animation.FuncAnimation(self.fig, self.animate,\
                                       init_func=self.init_animation,\
                                       interval=600, blit=False)
        plt.show()

    def init_animation(self):
        for animalName, animal in self.animals.iteritems():
            self.zooPlot.append(Line2D([animal[u'x']],\
                                       [animal[u'y']],\
                                       color=animal[u'animal'].color,\
                                       marker=animal[u'animal'].marker,\
                                       markersize=16))
            self.ax.add_line(self.zooPlot[-1])
        return tuple(self.zooPlot)

    def animate(self, step):
        self.move()
        self.zooPlot = []
        self.ax.cla()
        for x in range(self.width):
            for y in range(self.width):
                if self.area[x][y][0] == 'food':
                    self.zooPlot.append(Line2D([x], [y],\
                                               color='#D8F0DB',\
                                               marker='s',\
                                               markersize=16,\
                                               markeredgewidth=0))
                    self.ax.add_line(self.zooPlot[-1])
        for animalName, animal in self.animals.iteritems():
            self.zooPlot.append(Line2D([animal[u'x']],\
                                       [animal[u'y']],\
                                       color=animal[u'animal'].color,\
                                       marker=animal[u'animal'].marker,\
                                       markersize=16))
            self.ax.add_line(self.zooPlot[-1])
        time.sleep(0.1)
        return tuple(self.zooPlot)
    
    def move(self):
        self.battles = []
        for animalName in self.animals:
            animalMap = self.get_map(animalName)
##            self.messages.append('Map for ' + animalName +\
##                                 ': ' + str(animalMap))
            self.animals[animalName]['move'] =\
                        self.interpret_move(self.animals[animalName]['animal']
                                            .move(animalMap),
                                            animalName)
##            self.messages.append('Corrected return value from ' + animalName +\
##                                 ': ' + str(self.animals[animalName]['move']))
        self.fill_combatants()
        self.run_battles()
        self.move_animals()
        self.decrease_food()
        self.regenerate_food()
        self.reproduce_animals() # breed here.
        for message in self.messages:
            print message
        self.messages = []
        self.nTurn += 1
        print 'Turn ' + str(self.nTurn) + ' complete.'

    def reproduce_animals(self):
        """ Call the give_birth() method from
            some of the animals if it's possible to place
            the new animal beside the parent. """
        newAnimals = []
        disqualified = []
        for animalName in self.animals:
            if random.randint(1, 100) > 99: # Just because.
                animal = self.animals[animalName]['animal']
                try:
                    newAnimal = animal.give_birth()
                except:
                    self.messages.append('The animal ' + animal.name +\
                                 ' should be disqualified as give_birth() method failed.')
                    disqualified.append(animalName)
                    continue
                if newAnimal is animal:
                    self.messages.append('The animal ' + animal.name +\
                                 ' gave birth to itself. No animal added.')
                    continue
                newAnimal.marker = animal.marker
                tup = newAnimal, self.animals[animalName]['x'], self.animals[animalName]['y']
                newAnimals.append(tup)
        for animalName in disqualified: # kill all the animals disqualified.
            self.kill_animal(animalName)
        for tup in newAnimals: # add all the newborn.
            self.add_newborn(*tup)

    def add_newborn(self, newAnimal, x, y):
        try:
            if (newAnimal.speed + newAnimal.attack + newAnimal.defense != 100) or\
               newAnimal.speed < 0 or newAnimal.attack < 0 or\
               newAnimal.defense < 0:
                self.messages.append('The newborn animal ' + newAnimal.name +\
                                     ' has been disqualified.')
                return
        except:
            self.messages.append('The newborn animal ' + newAnimal.name +\
                                 ' doesn\'t have all required properties.')
            return
        newAnimal.food = 15
        possibleXcoords = range(x - 1, x + 2)
        possibleYcoords = range(y - 1, y + 2)
        freeCells = [(x, y) for x in range(self.width)\
                            for y in range(self.width)\
                     if self.area[x][y][1] == None and x in possibleXcoords and y in possibleYcoords]
        if len(freeCells) <= 0:
            self.messages.append('There are no free cells. Impossible to place a new animal.')
            return
        newName = newAnimal.name + u'__' + str(self.new_animal_number(newAnimal.name))
        x, y = random.choice(freeCells)
        self.area[x][y] = (self.area[x][y][0], newName)
        self.animals[newName] = {'animal': newAnimal,\
                                 'x': x,\
                                 'y': y,\
                                 'move': ('move', (x, y))}
        self.messages.append('Animal ' + newAnimal.name + ' born.')


    def fill_combatants(self):
        disputedCells = {}  # (x, y) -> [list of animals]
        for animalName in self.animals:
            if self.animals[animalName]['move'][0] == 'attack':
                self.add_battle([(self.animals[animalName]['x'],\
                                  self.animals[animalName]['y']),\
                                 self.animals[animalName]['move'][1]],\
                                'attack')
            elif self.animals[animalName]['move'][0] == 'move':
                try:
                    disputedCells[self.animals[animalName]['move'][1]].append(animalName)
                except KeyError:
                    disputedCells[self.animals[animalName]['move'][1]] = [animalName]
        for cell in disputedCells:
            if len(disputedCells[cell]) > 1:
                animalsCoord = [(self.animals[animalName]['x'],\
                                 self.animals[animalName]['y'])\
                                for animalName in disputedCells[cell]]
                animalsCoord.append(cell)
                self.add_battle(animalsCoord, 'disputedCell')

    def add_battle(self, animalsCoord, battleType):
        animalsCoord = set(animalsCoord)
        for battle in self.battles:
            if battle['coords'] == animalsCoord:
                return
        self.battles.append({'coords': animalsCoord, 'type': battleType})
        self.messages.append('Battle added: ' + str(animalsCoord))

    def run_battle(self, battle):
        combatants = []
        for coord in battle['coords']:
            try:
                animalName = self.area[coord[0]][coord[1]][1]
                animal = self.animals[animalName]
            except:
                continue # disputed cell with no animals in it
            if animal['move'][0] == 'attack' or\
               (animal['move'][0] == 'move' and battle['type'] == 'disputedCell'):
                rating = animal['animal'].attack
                flee = False
            elif animal['move'][0] == 'move' and battle['type'] == 'attack':
                rating = animal['animal'].defense
                flee = True
            elif animal['move'][0] == 'eat':
                rating = animal['animal'].defense
                flee = False
            combatants.append({u'name': animalName,\
                               u'rating': rating,\
                               u'flee': flee})
        if all([self.animals[combatants[i]['name']]['animal'].name ==\
                self.animals[combatants[i + 1]['name']]['animal'].name\
                for i in range(len(combatants) - 1)]):
            # Animals of the same species cannot fight
            for combatant in combatants:
                self.stop_animal(combatant['name'])
            return
        
        for i in range(len(combatants))[::-1]:
            animal = self.animals[combatants[i]['name']]
            if combatants[i]['flee']:
                flee = ddistr([(True, animal['animal'].speed / 100.0),\
                               (False, 1.0 - animal['animal'].speed / 100.0)])
                if flee:
                    self.move_animal(combatants[i]['name'])
                    del combatants[i]
        denominator = float(sum([c['rating'] for c in combatants]) + 20)
        probabilities = []
        for combatant in combatants:
            probabilities.append((combatant['name'], combatant['rating'] / denominator))
        probabilities.append((None, 20 / denominator))
        winner = ddistr(probabilities)
        if winner == None:
            for combatant in combatants:
                self.stop_animal(combatant['name'])
        else:
            for combatant in combatants:
                if combatant['name'] != winner:
                    if self.animals[combatant['name']]['animal'].name ==\
                       self.animals[winner]['animal'].name:
                        self.stop_animal(combatant['name'])
                    else:
                        self.kill_animal(combatant['name'])
                else:
                    self.move_animal(combatant['name'])
                    
                
    def run_battles(self):
        combatants = []
        for battle in self.battles:
            self.run_battle(battle)

    def new_animal_number(self, animalName):
        specifiers = [re.sub(u'^' + re.escape(animalName) + u'__', u'', n)\
                      for n in self.animals.keys() if animalName in n]
        if len(specifiers) == 0:
            newNumber = 0
        else:
            newNumber = max([int(s) for s in specifiers\
                             if re.search(u'^[0-9]+$', s) != None])
            newNumber += 1
        return newNumber
            
    def add_animal(self, animal):
        try:
            if (animal.speed + animal.attack + animal.defense != 100) or\
               animal.speed < 0 or animal.attack < 0 or\
               animal.defense < 0:
                self.messages.append('The animal ' + animal.name +\
                                     ' has been disqualified.')
                return
        except:
            self.messages.append('The animal ' + animal.name +\
                                 ' doesn\'t have all required properties.')
            return

        animal.food = 15
        freeCells = [(x, y) for x in range(self.width)\
                            for y in range(self.width)\
                     if self.area[x][y][1] == None]
        if len(freeCells) <= 0:
            self.messages.append('There are no free cells.')
            return
        newName = animal.name + u'__' + str(self.new_animal_number(animal.name))
        x, y = random.choice(freeCells)
        self.area[x][y] = (self.area[x][y][0], newName)
        self.animals[newName] = {'animal': animal,\
                                 'x': x,\
                                 'y': y,\
                                 'move': ('move', (x, y))}

    def move_animals(self):
        for animalName in self.animals:
            self.move_animal(animalName)

    def decrease_food(self):
        starvingAnimals = []
        for animalName in self.animals:
            self.animals[animalName]['animal'].food -= 0.25
            if self.animals[animalName]['animal'].food < 0:
                starvingAnimals.append(animalName)
        for animalName in starvingAnimals:
            self.messages.append('Animal ' + animalName + ' is starving.')
            self.kill_animal(animalName)
        
    def regenerate_food(self):
        for y in range(self.width):
            for x in range(self.width):
                if self.area[x][y][0] == 'desert':
                    probabilities = [('desert', 0.995), ('food', 0.005)]
                    newTerrain = ddistr(probabilities)
                    self.area[x][y] = (newTerrain, self.area[x][y][1])

    def kill_animal(self, animalName):
        self.area[self.animals[animalName]['x']][self.animals[animalName]['y']] =\
            (self.area[self.animals[animalName]['x']][self.animals[animalName]['y']][0], None)
        del self.animals[animalName]
        self.messages.append('animal ' + animalName + ' has been killed.')

    def move_animal(self, animalName):
        if self.animals[animalName]['move'][0] == 'eat':
            self.area[self.animals[animalName]['x']][self.animals[animalName]['y']] = ('desert', animalName)
            self.animals[animalName]['move'] = ('move', (self.animals[animalName]['x'],\
                                                         self.animals[animalName]['y']))
            self.animals[animalName]['animal'].food += 1.25
        self.area[self.animals[animalName]['x']][self.animals[animalName]['y']] =\
            (self.area[self.animals[animalName]['x']][self.animals[animalName]['y']][0], None)
        self.area[self.animals[animalName]['move'][1][0]][self.animals[animalName]['move'][1][1]] =\
            (self.area[self.animals[animalName]['move'][1][0]][self.animals[animalName]['move'][1][1]][0], animalName)
        self.animals[animalName]['x'] = self.animals[animalName]['move'][1][0]
        self.animals[animalName]['y'] = self.animals[animalName]['move'][1][1]

    def stop_animal(self, animalName):
        self.animals[animalName]['move'] = ('move', (self.animals[animalName]['x'],\
                                                     self.animals[animalName]['y']))

    def interpret_move(self, returnTuple, animalName):
##        self.messages.append('Original return value from ' + animalName +\
##                             ': ' + str(returnTuple))
        if type(returnTuple) != tuple or\
           len(returnTuple) != 2 or\
           (type(returnTuple[0]) != str and type(returnTuple[0]) != unicode) or\
           type(returnTuple[1]) != int or\
           returnTuple[1] < 0 or returnTuple[1] > 8:
            self.messages.append(animalName + u' returned wrong value.')
            return ('move', (self.animals[animalName]['x'],\
                             self.animals[animalName]['y']))
        if returnTuple[0] == 'eat':
            returnTuple = ('eat', 4)
        absDirection = self.abs_coord(returnTuple[1], animalName)
        if returnTuple[0] != 'eat' and\
           self.area[absDirection[0]][absDirection[1]][1] != None and\
           self.area[absDirection[0]][absDirection[1]][1] != animalName:
            return ('attack', absDirection)
        return (returnTuple[0].strip().lower(), absDirection)

    def abs_coord(self, direction, animalName):
        newX = self.animals[animalName]['x'] + direction % 3 - 1
        newY = self.animals[animalName]['y'] + direction / 3 - 1
        return (newX, newY)

    def get_map(self, animalName):
        xCentre = self.animals[animalName]['x']
        yCentre = self.animals[animalName]['y']
        returnMap = []
        for y in range(3):
            for x in range(3):
                relX = xCentre + x - 1
                relY = yCentre + y - 1
                if relX < 0 or relX >= self.width or\
                   relY < 0 or relY >= self.width:
                    returnMap.append(('fence', None))
                elif self.area[relX][relY][1] != None and\
                     (relX != xCentre or relY != yCentre):
                    returnMap.append(('animal', self.animals[self.area[relX][relY][1]]['animal']))
                else:
                    returnMap.append((self.area[relX][relY][0], None))
        return returnMap

    def print_picture(self):
        pic = ''
        for y in range(self.width):
            for x in range(self.width):
                if self.area[x][y][1] != None:
                    pic += self.area[x][y][1][0]    # first letter
                elif self.area[x][y][0] == 'desert':
                    pic += ' '
                elif self.area[x][y][0] == 'food':
                    pic += '.'
                else:
                    pic += '?'  # this should never happen normally
            pic += '\n'
        os.system('cls')
        print pic

