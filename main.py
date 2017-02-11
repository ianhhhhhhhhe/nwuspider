from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from nwu.spiders.nwu_spider import NWUSpider
from nwu.spiders.nwulab_spider import NWUlabSpider

process = CrawlerProcess(get_project_settings())

runner = CrawlerRunner()
runner.crawl(NWUSpider)
runner.crawl(NWUlabSpider)

d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()
