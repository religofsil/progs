# -*- coding: utf-8 -*-

class University:
    def __init__(self, students):
        self.students = students
        self.hymn = 'lalala-la-lala-la-laaaaa, our university is the best university'
        self.vipuskniki = []

    def add_student(self, name, surname, department):
        student=Student(name, surname, u'1 бак', department)
        self.students.append(student)

    def end_year(self):
        for student in self.students:
            if student.next_year() == False:
                self.vipuskniki.append(student)
        for vipusknik in self.vipuskniki:
            self.students.remove(vipusknik)


class Student(University):
    def __init__(self, name, surname, year, department):
        self.name = name
        self.surname = surname
        self.year = year
        self.department = department
        self.y = int(self.year.split(' ')[0])
        self.bm = self.year.split(' ')[1]

    def __lt__(self, other):
        if self.bm == other.bm:
            return self.y < other.y
        else:
            if self.bm == u'бак':
                return True
            else:
                return False

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __gt__(self, other):
        return __lt__(self, other) == False and __eq__(self, other) == False

    def __ge__(self, other):
        return __lt__(self, other) == False

    def __le__(self, other):
        return __gt__(self, other) == False

    def next_year(self):
        if self.year != u'2 маг':
            if self.y < 4:
                self.y += 1
                self.year = str(self.y) + u' ' + self.bm
                return True
            else:
                self.y = 1
                self.bm = u'маг'
                self.year = u'1 маг'
                return True
        else:
            return False


s1 = Student('Sasha', 'Ershova', u'3 бак', 'ling')
s2 = Student('Masha', 'Ivanova', u'2 маг', 'ling')
s3 = Student('Imya', 'Familiya', u'4 бак', 'ling')
s4 = Student('Imya2', 'Familiya2', u'1 бак', 'ling')
s5=Student('X', 'Y', u'1 маг', 'ling')
hse = University([s1, s2, s3, s4, s5])
hse.end_year()
for i in sorted(hse.students):
    print i.name, i.year
