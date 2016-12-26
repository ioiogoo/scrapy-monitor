# -*- coding: utf-8 -*-

'''
    添加
    DOWNLOADER_MIDDLEWARES      monitor.statscol.StatcollectorMiddleware    中间件，详细请看statscol.py
    ITEM_PIPELINES              monitor.statscol.SpiderRunStatspipeline     发送spider启用和关闭的信息
    STATS_KEYS                  需要收集的爬虫状态信息字段
'''
BOT_NAME = 'visiter'

SPIDER_MODULES = ['visiter.spiders']
NEWSPIDER_MODULE = 'visiter.spiders'



ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 0.33

DEFAULT_REQUEST_HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


DOWNLOADER_MIDDLEWARES = {
   'visiter.monitor.statscol.StatcollectorMiddleware': 200,
}


ITEM_PIPELINES = {
    'visiter.pipelines.VisiterPipeline': 300,
    'visiter.monitor.statscol.SpiderRunStatspipeline': 301
}

STATS_KEYS = ['downloader/request_count', 'downloader/response_count','downloader/response_status_count/200', 'item_scraped_count']

