# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 2016/12/25 16:50
'''

import redis
from .settings import STATS_KEYS
import time
import requests

r = redis.Redis(host='localhost', port=6379, db=0)
Time = lambda: time.strftime('%Y-%m-%d %H:%M:%S')


class StatcollectorMiddleware(object):
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)
        self.stats_keys = STATS_KEYS

    def process_request(self, request, spider):
        self.formatStats(spider.crawler.stats.get_stats())

    def formatStats(self, stats):
        for key in self.stats_keys:
            key_value = stats.get(key, None)
            if not key_value: continue
            value = {"value": [Time(), key_value]}
            self.insert2redis(key, value)

    def insert2redis(self, key, value):
        self.r.rpush(key, value)


class SpiderRunStatspipeline(object):
    def open_spider(self, spider):
        r.set('spider_is_run', 1)
        requests.get('http://127.0.0.1:5000/signal?sign=running')

    def close_spider(self, spider):
        r.set('spider_is_run', 0)
        requests.get('http://127.0.0.1:5000/signal?sign=closed')