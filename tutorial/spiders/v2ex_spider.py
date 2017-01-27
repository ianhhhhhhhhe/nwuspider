# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import V2EXItem

class DmozSpider(scrapy.Spider):
    name = "v2ex"
    allowed_domains = ["v2ex.com"]
    start_urls = [
        "https://www.v2ex.com/?tab=tech",
        "https://www.v2ex.com/go/python",
        "https://www.v2ex.com/?tab=creative",
    ]

    def parse(self, response):
        for sel in response.xpath('//span[@class="item_title"]'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            if not item['title']:
                continue
            yield item
