# coding=utf-8
import lxml.html
import codecs
import os
import urllib2
import HTMLParser


def save_to_file(texts):
    onestring = ''
    for i in texts:
        # print '__%s__' % (i)
        onestring += i
    f = codecs.open(u'corpora.txt', 'a', 'utf-8-sig')
    f.write(onestring + u'\n')
    f.close()


def get_links_contin(root):
    """получает на вход страницу-узел и возвращает ссылки с продолжением статьи"""
    block = root.xpath('//div[@class="entry-pagination pagination"]')
    if len(block) == 1:
        linx = [x.get('href') for x in block[0].xpath('.//a')]
        return linx
    else:
        return None

def crawl_on_the_page(link):
    print u'залезаем на страницу %s' % link
    req = urllib2.Request(link, headers={'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10"})
    text = urllib2.urlopen(req).read()
    root = lxml.html.fromstring(text)
    texts=[x.text_content() for x in root.xpath('//div[@class="intro"]')]
    #texts = [x.text_content() + u' ' for x in root.xpath('//p') if x.text_content() != None]
    #texts += [x.text_content() + u' ' for x in root.xpath('//h2')]
    save_to_file(texts)
    #return root

def crawlroot(link):
    req = urllib2.Request(link, headers={'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10"})
    text = urllib2.urlopen(req).read()
    root = lxml.html.fromstring(text)
    return root

def fixlink(link):
    link='http://www.realisti.ru'+link
    return link

def getlinks(root):
    block = root.xpath('//div[@class="text"]/a')
    linx = []
    for i in block:
        linx.append(fixlink(i.get('href')))
    return linx

def main():
    f = codecs.open(u'corpora.txt', 'w', 'utf-8-sig')
    f.close()
    link = u'http://www.realisti.ru/main/spirit'
    root = crawlroot(link)
    artic=getlinks(root)
    for i in artic:
        crawl_on_the_page(i)

main()
