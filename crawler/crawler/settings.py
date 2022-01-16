BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'



USER_AGENT = 'crawler (+http://www.yourdomain.com)'


ROBOTSTXT_OBEY = True


CONCURRENT_REQUESTS = 1


DOWNLOAD_DELAY = 3


ITEM_PIPELINES = {
   'crawler.pipelines.CrawlerPipeline': 300,
}

import sys
sys.path.append('/Users/taguchiryuma/TechsonTest')
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
# If you you use django outside of manage.py context, you
# need to explicitly setup the django
import django
django.setup()