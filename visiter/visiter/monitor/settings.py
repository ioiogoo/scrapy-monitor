# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 2016/12/26 11:48
'''

'''
    TIMEINTERVAL        刷新时间间隔，单位毫秒
    POINTINTERVAL       图上各点之间间隔，越小则表示点越密集
    POINTLENGTH         图上点的数量，越大则表示图上时间跨度越长
    STATS_KEYS          图上显示的stats_key
    REDIS_HOST          redis地址
    REDIS_PORT          redis端口
    REDIS_DB            redis数据库，默认0
    APP_HOST            app运行地址，默认127.0.0.1
    APP_PORT            app运行端口，默认5000
'''

TIMEINTERVAL = 1000
POINTINTERVAL = 30
POINTLENGTH = 2000
STATS_KEYS = ['downloader/request_count', 'downloader/response_count','downloader/response_status_count/200', 'item_scraped_count']
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
APP_HOST = '127.0.0.1'
APP_PORT = 5000
