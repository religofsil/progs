# -*- coding: utf-8 -*-
import lxml.html, re


def get_first(root, child_tag, class_attr=None):
    for child in root.findall(child_tag):
        if class_attr is None or child.get('class') == class_attr:
            return child


def fuskator(string):
    if string is not None:
        string = string.text_content()
        string = re.sub('hseEObfuscator\(\n', '', string)
        string = re.split('\],\[', string)
        string = string[-1]
        string = re.sub('\t|"|\[|\]|,', '', string)
        string = re.sub('[);\n\r]', '', string)
        return string
    else:
        return None


def persons_blocks_lxml(html):
    root = lxml.html.fromstring(html)
    body = get_first(root, 'body')
    page = get_first(body, 'div', 'page')
    subpage = get_first(page, 'div', 'layout medium')
    grid = get_first(subpage, 'div', 'grid')
    cont = get_first(grid, 'div', 'main content')
    subcont = get_first(cont, 'div')
    persons = get_first(subcont, 'div', 'posts persons')
    subpersons = persons.findall('div')[1]
    results = []
    for person in subpersons.findall('div'):
        if person.get('class') == 'post person':
            results.append(Person(person))
    return results


class Person:
    def __init__(self, string):
        self.string = string
        self.phoneandmail = string[0][0]
        self.phone = self.phoneandmail.text
        self.email = get_first(self.phoneandmail, 'script')
        self.email = fuskator(self.email)
        self.nameandoccupation = get_first(string[0], 'div', 'main content small')
        self.name = self.nameandoccupation[0][0].text_content().split(' ')
        self.lastname = self.name[0]
        if len(self.name) > 1:
            self.firstname = self.name[1]
            if len(self.name) > 2:
                self.fathername = self.name[2]
            else:
                self.fathername = None
        else:
            self.fathername = None
            self.lastname = None
        self.occupation = self.nameandoccupation[0][1].text_content()


def main():
    with open('person-k.html') as f:
        html = f.read().decode('utf-8')
    blocks = persons_blocks_lxml(html)
    for i in blocks:
        print i.phone


main()
