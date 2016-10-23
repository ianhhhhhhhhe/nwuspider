# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import NWUItem

class NwulabSpiderSpider(scrapy.Spider):
    name = "nwulab"
    allowed_domains = ["ipc.nwu.edu.cn"]
    start_urls = ['http://ipc.nwu.edu.cn/']

    def parse(self, response):

        for sel in response.xpath('//*[@id="main"]/div/p'):
            item = NWUItem()
            item['title'] = sel.xpath('strong/a/text()').extract()
            item['link'] = sel.xpath('strong/a/@href').extract()
            yield item
