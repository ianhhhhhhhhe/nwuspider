# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import NWUItem

class NwuSpiderSpider(scrapy.Spider):
    name = "nwu"
    allowed_domains = ["nwu.edu.cn"]
    start_urls = [
        "http://www.nwu.edu.cn/",
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="newslist"]/li'):
            item = NWUItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            if not item['title']:
                continue
            my_logger.info(item)
            yield item
