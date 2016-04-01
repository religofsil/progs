# -*- coding: utf-8 -*-

import lxml.html, re


def fuskator(string):
    if string is not None:
        string = re.sub('hseEObfuscator\(\n', '', string)
        string = re.split('\],\[', string)
        string = string[-1]
        string = re.sub('\t|"|\[|\]|,', '', string)
        string = re.sub('[);\n\r]', '', string)
        string = re.sub(' ', '', string)
        return string
    else:
        return None


class Person:
    def __init__(self, string):
        self.name = string.xpath('//div[@class="main content small"]/div/a/div')[0].get('title').split(' ')
        try:
            self.firstname = self.name[1]
        except:
            self.firstname = None
        self.lastname = self.name[0]
        try:
            self.fathername = self.name[2]
        except:
            self.fathername = None
        try:
            self.phone = string.xpath('//div[@class="l-extra small"]')[0].text
        except:
            self.phone = None
        try:
            self.mail = fuskator(string.xpath('//div[@class="l-extra small"]/script')[0].text)
        except:
            self.mail = None
        try:
            self.occupation = string.xpath('//div[@class="content__inner content__inner_foot1"]/p')[0].text_content()
        except:
            self.occupation = None


def persons_blocks_lxml(html):
    html = lxml.html.fromstring(html)
    arr = html.xpath('//div[@class="post person"]')
    results = []
    for person in arr:
        results.append(Person(person))
    return results


def main():
    with open('person-a.html') as f:
        html = f.read().decode('utf-8')
    blocks = persons_blocks_lxml(html)
    print blocks[0].firstname


main()