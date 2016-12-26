# scrapy monitor
针对scrapy框架设计的实时监控爬虫状态系统。

使用了Flask开启web服务，将实时状态保存在redis数据库中

# 效果展示
![](https://github.com/ioiogoo/scrapy-monitor/blob/master/爬虫监控.jpg)

* 数据实时更新，可设置时间间隔
* 图表可下载保存
* 图表放大至局部
* 监控数据类型可控
* 监控时间范围可控

# 项目依赖
* scrapy
* redis数据库
* redis包
* flask框架

# 使用方法

将monitor目录clone到spiders的同级目录下

## scrapy settings.py
* 添加`DOWNLOADER_MIDDLEWARES`
    * monitor.statscol.StatcollectorMiddleware
* 添加`ITEM_PIPELINES`
    * monitor.statscol.SpiderRunStatspipeline
* 添加`STATS_KEYS`
    * STATS_KEYS = ['downloader/request_count', 'downloader/response_count','downloader/response_status_count/200', 'item_scraped_count']

## monitor settings.py
```
    TIMEINTERVAL        刷新时间间隔，单位毫秒
    POINTINTERVAL       图上各点之间间隔，越大则表示点越密集
    POINTLENGTH         图上点的数量，越大则表示图上时间跨度越长
    STATS_KEYS          图上显示的stats_key
    REDIS_HOST          redis地址
    REDIS_PORT          redis端口
    REDIS_DB            redis数据库，默认0
    APP_HOST            app运行地址，默认127.0.0.1
    APP_PORT            app运行端口，默认5000
```
默认即可

运行你的爬虫项目，再运行monitor.app即可看到监控画面

# 实现原理

## 爬虫状态收集
`StatcollectorMiddleware`中间件在每个request发出时将当前crawler的stats保存到redis。

## 前端数据可视化
ajax实时请求当前状态信息，flask从redis中取出需要的信息，用Echart渲染出图片。
图片可放大查看局部信息，可保存当前监控信息。

