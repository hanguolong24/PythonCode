#!/usr/bin/env python
#-*-coding:utf-8 -*-
#Time:2018/4/26  16:58
#Author:Kevin Hon
#--------------------------------------------------
from requests_html import *

'''01-抓取一个网站上的所有链接打印出来'''
# session = HTMLSession()
# r = session.get('https://python.org/')
# # 获取页面上的所有链接。
# all_links =  r.html.links
# print(all_links)
# # 获取页面上的所有链接，以绝对路径的方式。
# all_absolute_links = r.html.absolute_links
# print(all_absolute_links)


'''02-抓取cnblogs网站上的最新更新的新闻打印链接和标题'''
from requests_html import HTMLSession
def GetLinks():
    session = HTMLSession()
    r = session.get(url)
    news = r.html.find('.items-area dl dt a')
    # for new in news:
    #     print(new.text)
    #     print(new.absolute_links)
    fp = open(file_path, "w+")
    for new in news:
        fp.write(str(new.text) + "\n")
        fp.write(str(new.absolute_links) + "\n")
    fp.close()


if __name__ == '__main__':
    url = 'https://www.cnbeta.com'
    file_path = "d:\\CrawlerNews.txt"
    GetLinks()



