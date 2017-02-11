# -*- coding: utf-8 -*-

# Scrapy settings for nwu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'nwu'

SPIDER_MODULES = ['nwu.spiders']
NEWSPIDER_MODULE = 'nwu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'nwu (+http://www.yourdomain.com)'

# Cookies Config
COOKIES_DEBUG = False
COOKIES_ENABLED = False

# Feed Export
FEED_URI = 'nwu.csv'
FEED_FORMAT = 'CSV'

# Logging Config
LOG_ENABLED = False
LOG_ENCODING = 'utf-8'
LOG_FILE = 'NWUSpider.out'
LOG_LEVEL = 'DEBUG'
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
LOG_STDOUT = True

# Item Pipeline Config
ITEM_PIPELINES = {
    'nwu.pipelines.JsonWriterPipeline': 700,
}

# Notification e-mail address
MEMUSAGE_NOTIFY_MAIL = ['user@test.com']
