# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Cookies Config
COOKIES_DEBUG = False
COOKIES_ENABLED = False

# Logging Config
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_LEVEL = 'INFO'

# Item Pipeline Config
ITEM_PIPELINES = {
    'tutorial.pipelines.JsonWriterPipeline': 700,  
}
