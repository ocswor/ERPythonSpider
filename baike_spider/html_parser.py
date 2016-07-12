__author__ = 'eric'
# encoding: utf-8
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
class HtmlParser:
    def parse(self, url, content):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8')
        new_urs = self._get_new_urls(url,soup)
        new_data = self._get_new_data(url,soup)

        return new_urs,new_data

    def _get_new_urls(self, page_url, soup):
        links = soup.find_all('a',href = re.compile(r'/view/\d+\.htm'))
        new_urls = set()
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url,new_url)
            new_urls.add(new_full_url)

        return new_urls


    def _get_new_data(self, url, soup):
        res_data = {}
        res_data['url'] = url

        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data





# help(urlparse)
content = """
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link2">
    Tillie
   </a>
   ; and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
"""

# soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
# print('获取所有的链接')
# links = soup.find_all('a')
# for link in links:
#     print(link.name, link['href'], link.get_text())
#
# print('获取lacie的链接')
#
# # link_node = soup.find('a', href=re.compile(r"tille"))
# # print(link_node.name, link_node['href'], link_node.get_text())
#
# print('获取tille的链接')
# # line_test = soup.findAll(name='a', attrs={"href": re.compile(r'tille')})
# line_test = soup.find('a', href="http://example.com/lacie")
# print(line_test.name, line_test['href'], line_test.get_text())
