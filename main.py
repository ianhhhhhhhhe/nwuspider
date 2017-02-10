from scrapy.crawler import CrawlerProcess
from tutorial.spiders.v2ex_spider import V2EXSpider
from tutorial.spiders.nwu_spider import NWUSpider
from tutorial.spiders.nwulab_spider import NWUlabSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13'
})

process.crawl(V2EXSpider)
process.crawl(NWUSpider)
process.crawl(NWUlabSpider)
process.start()
