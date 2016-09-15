__author__ = 'Sasha'

class Student:
    def __init__(self):
        self.name=u''
s=Student()
s.name='John Smith'
print s.name

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance(self, n):
        d=((self.x-n.x)**2+(self.y-n.y)**2)**0.5
        return d

p=Point(3,4)
p2=Point(6,10)
print p.distance(p2)