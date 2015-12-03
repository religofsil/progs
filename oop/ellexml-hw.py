# -*- coding: utf-8 -*-
import re, lxml.html
# В этот раз домашнее задание опять состоит в том,
# чтобы доделать то, что мы делали в классе.
# Нужно, чтобы в программе был класс преподавателя
# (который можно просто взять из предыдущей домашки,
# если он там нормально работает) и чтобы создавался массив преподавателей.
# Информация о преподавателях должна извлекаться из предварительно сохранённой
# HTML-страницы с помощью модуля lxml.
# Понятно, что всё сделать с помощью lxml не удастся --
# например, восстанавливать адрес электронной почты из
# хитрого закодированного вида придётся как-то по-другому, --
# но всё, что можно сделать с помощью lxml, должно быть сделано с помощью lxml.

def get_first(root, child_tag, class_attr=None):
    for child in root.findall(child_tag):
        if class_attr is None or child.get('class') == class_attr:
            return child

class Person:
    def __init__(self, string):
        self.person=string
        root=lxml.html.fromstring(string)
        root=root[0]
        print root.tag
        root=root[0]
        print root.tag
        root=root[1]
        print root.tag
        root=root[0]
        print root.tag
        root=root[0]
        root=root[0]
        self.fullname=root.get('title')

test=Person('''<div class="post person">
<div class="post__content post__content_person">
    <div class="l-extra small">+7 (495) 772-95-90*22073<br><script>hseEObfuscator(
								["a","b","a","n","k","i","n","a","i","@","h","s","e",".","r","u"]
							);</script></div>
    <div class="main content small"><div class="content__inner content__inner_foot1">
        <a href="/org/persons/25477" class="link link_dark large b"><div class="g-pic person-avatar-small2" style="background-image: url(/data/2010/09/15/1234592087/2%D0%98%D1%80%D0%B8%D0%BD%D0%B0%20%D0%90%D0%B1%D0%B0%D0%BD%D0%BA%D0%B8%D0%BD%D0%B0.jpg);" title="Абанкина Ирина Всеволодовна" alt="Абанкина Ирина Всеволодовна"></div>Абанкина Ирина Всеволодовна</a><p class="with-indent7">Профессор: <a class="link" href="http://ioe.hse.ru/">Институт образования</a> / <a class="link" href="http://ioe.hse.ru/po">Департамент образовательных программ</a><br>Директор: <a class="link" href="http://ioe.hse.ru/">Институт образования</a> / <a class="link" href="http://iro.hse.ru/">Институт развития образования</a></p><div class="with-indent small"><a class="tag" href="/org/persons/?intst=562677">человеческий капитал</a><a class="tag" href="/org/persons/?intst=79203">образовательные стандарты</a><a class="tag" href="/org/persons/?intst=79192">экономика образования</a><a class="tag" href="/org/persons/?intst=3266046">финансирование образования</a><a class="tag" href="/org/persons/?intst=24812">образовательная политика</a><a class="tag" href="/org/persons/?intst=1295521">реформа образования</a><a class="tag" href="/org/persons/?intst=56002585">образовательное право</a></div></div></div></div></div><div class="post person"><div class="post__content post__content_person"><div class="l-extra small">+7 (495) 772-95-90<br><script>hseEObfuscator(
								["a","b","a","n","k","i","n","a","t","@","h","s","e",".","r","u"]
							);</script></div>
	<div class="main content small"><div class="content__inner content__inner_foot1"><a href="/org/persons/203662" class="link link_dark large b"><div class="g-pic person-avatar-small2" style="background-image: url(/data/2011/02/18/1234508124/7DSC04470.JPG);" title="Абанкина Татьяна Всеволодовна" alt="Абанкина Татьяна Всеволодовна"></div>Абанкина Татьяна Всеволодовна</a><p class="with-indent7">Профессор: <a class="link" href="http://ioe.hse.ru/">Институт образования</a> / <a class="link" href="http://ioe.hse.ru/po">Департамент образовательных программ</a><br>Директор центра: <a class="link" href="http://www.hse.ru/pubresource/">Институт управления государственными ресурсами</a> / <a class="link" href="http://www.hse.ru/pubresource/">центр государственного сектора экономики</a></p><div class="with-indent small"><a class="tag" href="/org/persons/?intst=158761720">Экономика и управление социальной сферой,</a><a class="tag" href="/org/persons/?intst=158761893">экономика образования и культуры, творческие индустрии, частно-государственное партнерство</a></div></div></div></div></div>''')
print test.fullname