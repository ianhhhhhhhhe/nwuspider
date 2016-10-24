# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import V2EXItem

import glob
import logging
import logging.handlers

LOG_FILENAME = 'Spider.out'

my_logger = logging.getLogger('Mylogger')
my_logger.setLevel (logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                               maxBytes = 1048576,
                                               backupCount = 24,
                                               )
my_logger.addHandler(handler)

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
            my_logger.info(item)
            yield item
