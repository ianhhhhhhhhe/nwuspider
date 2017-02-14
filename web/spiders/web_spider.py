# -*- coding: utf-8 -*-
import scrapy
from web.items import WebItem

class webSpider(scrapy.Spider):
    name = "web"
    allowed_domains = ["web.edu.cn"]
    start_urls = [
        'http://www.web.edu.cn/',
        ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="newslist"]/li'):
            item = webItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item
