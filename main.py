from scrapy import cmdline
import os

os.chdir('py03_spider_day14/spiders')
cmdline.execute('scrapy runspider lagou.py'.split())