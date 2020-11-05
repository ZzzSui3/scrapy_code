# -*- coding: utf-8 -*-
import scrapy


class HtSpiderSpider(scrapy.Spider):
    name = 'ht_spider'
    # allowed_domains = ['']
    start_urls = ['https://wuhan.anjuke.com/sale/rd1/?kw=%E5%8D%97%E6%B9%96%E5%B0%8F%E5%8C%BA']

    def parse(self, response):

        # print(response.text)
        data = response.text
        with open('anjuke.html','w',encoding='utf8') as f:
            f.write(data)
