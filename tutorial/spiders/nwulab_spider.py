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


class NwulabSpiderSpider(scrapy.Spider):
    name = "nwulab"
    allowed_domains = ["ipc.nwu.edu.cn"]
    start_urls = ['http://ipc.nwu.edu.cn/']

    def parse(self, response):

        for sel in response.xpath('//*[@id="main"]/div/p'):
            item = NWUItem()
            item['title'] = sel.xpath('strong/a/text()').extract()
            item['link'] = sel.xpath('strong/a/@href').extract()
            if not item['title']:
                continue
            my_logger.info(item)
            yield item
