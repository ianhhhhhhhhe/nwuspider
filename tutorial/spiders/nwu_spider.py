# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import NWUItem

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
