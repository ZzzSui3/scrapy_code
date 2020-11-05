# -*- coding: utf-8 -*-
import scrapy


class YmxSpider(scrapy.Spider):
    name = 'ymx'
    allowed_domains = ['amazon.cn']
    start_urls = ['https://www.amazon.cn/s?k=键盘&page=1&ref=sr_pg_1']

    def parse(self, response):
        s_list = response.css('.a-size-base-plus.a-color-base.a-text-normal')
        print(len(s_list))
        for i in s_list:
            yield {
                'jieshao':i.css('::text').extract_first()
            }
        page_next = response.css("li.a-last a::attr(href)").extract_first()
        # print(page_next)
        if page_next is not None:
            page_next = response.urljoin(page_next)
            yield scrapy.Request(page_next,callback=self.parse)
