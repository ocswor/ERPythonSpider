from baike_spider import url_manager, html_downloader, html_parser, html_outputer

__author__ = 'eric'
# encoding: utf-8
# coding:utf8

print("哈哈")


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):

        count = 1

        # 将根url添加到url控制器
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():  # 开始业务循环,当url管理器中有新的url的时候
            try:
                new_url = self.urls.get_new_url()  # 获取一个新的url
                print('craw %d :%s' % (count, new_url))
                html_content = self.downloader.downloader(new_url)  # 下载器开始下载数据 获取html内容
                new_urls, new_data = self.parser.parse(new_url, html_content)  # 开始解析下载的内容,返回新的url集合 和获取的数据
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)  # 对解析到的数据进行输出处理

                if count == 100:
                    break

                count += 1
            except:
                print('craw failed')

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
