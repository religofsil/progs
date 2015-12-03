import lxml.html


def get_first(root, child_tag, class_attr=None):
    for child in root.findall(child_tag):
        if class_attr is None or child.get('class') == class_attr:
            return child


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
            results.append(person)
    return results


def main():
    with open('persons-a.html') as f:
        html = f.read().decode('utf-8')
    blocks = persons_blocks_lxml(html)
    print blocks[0].text_content()


main()
