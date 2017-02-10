from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from tutorial.spiders.nwu_spider import NWUSpider
from tutorial.spiders.nwulab_spider import NWUlabSpider

configure_logging()
runner = CrawlerRunner()
runner.crawl(NWUSpider)
runner.crawl(NWUlabSpider)

d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()
