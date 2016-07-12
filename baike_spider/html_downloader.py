__author__ = 'eric'
# encoding: utf-8
from urllib import request

class HtmlDownloader:
    def downloader(self, url):
        print(url)
        if url is None:
            return None

        response = request.urlopen(url)

        if response.getcode() != 200:
            return None
        return  response.read()



content = HtmlDownloader().downloader("http://baike.baidu.com/view/21087.htm")

print(content)