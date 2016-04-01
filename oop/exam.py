# -*- coding: utf-8 -*-
import re, lxml.html


class Tweet:
    def __init__(self, author='', text='', date='', retweets=0):
        self.author = author
        self.text = text
        if len(self.text) > 140:
            self.text = self.text[0:139]
        self.date = date
        self.retweets = retweets
        if self.retweets < 0:
            self.retweets = 0
        self.mentions = []
        self.hashtags = []

    def get_hashtags(self):
        self.hashtags = re.findall('(#[0-9A-ZА-ЯЁa-zа-яё_]+)', self.text)

    def get_mentions(self):
        self.mentions = re.findall('(@[0-9A-ZА-ЯЁa-zа-яё_]+)', self.text)

    def replace(self, whaat, wiith):
        if whaat in self.text:
            self.text = self.text.split(whaat)
            self.text = wiith.join(self.text)


def gettweets(html):
    html = lxml.html.fromstring(html)
    arr = html.xpath('//div[@data-component-term="tweet"]')
    results = []
    for tweet in arr:
        author = tweet[0][0][0][0][0][0].text_content()
        # text=tweet.xpath('//div[@class="ProfileTweet-contents"]')[0].text_content()
        text = tweet[0][0][0][1][0].text_content()
        results.append(Tweet(author, text))
    return results


def main():
    with open('obamatwitter.html') as f:
        html = f.read().decode('utf-8')
    blocks = gettweets(html)
    for i in blocks:
        i.get_mentions()
        print i.text
        for n in i.mentions:
            print n


main()
