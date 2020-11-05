# -*- coding: utf-8 -*-
import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    # allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/','http://www.baidu.com']

    # def start_requests(self):
    #     for url in self.start_urls:
    #         if 'baidu' in url:
    #             print('---------------------')
    #             yield scrapy.Request(url,callback=self.parse_baidu)
    #         else:
    #             yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        for url in self.start_urls:
            if 'baidu' in url:
                # print('---------------------')
                yield scrapy.Request(url,callback=self.parse_baidu)
            else:
                yield scrapy.Request(url)
        mingyans = response.css("div.quote")
        for mingyan in mingyans:
            text = mingyan.css(".text::text").extract_first()
            autor = mingyan.css(".author::text").extract_first()
            tags = mingyan.css(".tags .tag::text").extract()
            tags = ','.join(tags)

            print("标题:",text)
            print("作者:",autor)
            print("标签:",tags)
        # print('------------')
        next_page = response.css("li.next a::attr(href)").extract_first()
        print(next_page)

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)

    def parse_baidu(self,response):
        print('1\n'*15)
