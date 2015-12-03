from zoo import Zoo
from mypokemon import Charmander
from Andr2 import Rhino

z = Zoo()
a = Charmander()
b = Rhino()
a.color = '#2E4DFF'
a.marker = '<'
b.marker = '*'
for i in range(10):
    z.add_animal(a)
    z.add_animal(b)
z.start()
