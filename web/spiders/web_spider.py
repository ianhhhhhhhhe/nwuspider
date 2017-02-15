# -*- coding: utf-8 -*-
import scrapy
from web.items import WebItem

class webSpider(scrapy.Spider):
    name = "web"

    def start_requests(self):
        for url in self.settings.get('URLS'):
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for sel in response.xpath(self.settings.get('ROOT_PATH')):
            item = WebItem()
            item['title'] = sel.xpath(self.settings.get('ITEM_PATH')['TITLE']).extract()
            item['link'] = sel.xpath(self.settings.get('ITEM_PATH')['LINK']).extract()
            yield item
