from twisted.internet import reactor, defer

from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

import logging

from nwu.spiders.nwu_spider import NWUSpider
from nwu.spiders.nwulab_spider import NWUlabSpider

configure_logging(get_project_settings())
runner = CrawlerRunner(get_project_settings())

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(NWUSpider)
    yield runner.crawl(NWUlabSpider)
    reactor.stop()

crawl()
reactor.run()
