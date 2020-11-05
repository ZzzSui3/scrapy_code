# -*- coding: utf-8 -*-
import scrapy
import bs4
from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'top250'
    # allowed_domains = ['book.douban.com']
    start_urls = ['http://www.baidu.com']

    # for i in range(381):
    #     # url = "https://book.douban.com/top250?start=" + str(i * 25)
    #     url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T".format(str(i*20))
    #     start_urls.append(url)

    def parse(self, response):
        # 用BeautifulSoup解析response
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        # datas = bs.find_all("tr",class_="item")
        datas = bs.find_all("tr",class_="info")
        # print(type(datas),'='*30)

        for data in datas:
            item = DoubanItem()
            item["title"] = data.find_all("a")[1]["title"]
            # item["publish"] = data.find("p",class_='pl').text
            item["publish"] = data.find("div",class_='pub').text

            item["score"] = data.find("span",class_='rating_nums').text

            # print(item["title"])
            yield item