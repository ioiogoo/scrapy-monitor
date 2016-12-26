# -*- coding: utf-8 -*-
'''
Author = ioiogoo
Time = 2016/12/14 9:35
'''
from scrapy import Spider, Request
from bs4 import BeautifulSoup
import lxml
from ..items import VisiterItem

class visitorSpider(Spider):
    name = 'visitorSpider'

    def __init__(self):
        # self.proviceurl = ['http://www.361ok.com/jingdian/10010/','http://www.361ok.com/jingdian/10011/','http://www.361ok.com/jingdian/10012/','http://www.361ok.com/jingdian/10013/','http://www.361ok.com/jingdian/10014/','http://www.361ok.com/jingdian/10015/','http://www.361ok.com/jingdian/10016/','http://www.361ok.com/jingdian/10017/','http://www.361ok.com/jingdian/10018/','http://www.361ok.com/jingdian/10019/','http://www.361ok.com/jingdian/10020/','http://www.361ok.com/jingdian/10021/','http://www.361ok.com/jingdian/10022/','http://www.361ok.com/jingdian/10023/','http://www.361ok.com/jingdian/10024/','http://www.361ok.com/jingdian/10025/','http://www.361ok.com/jingdian/10026/','http://www.361ok.com/jingdian/10027/','http://www.361ok.com/jingdian/10028/','http://www.361ok.com/jingdian/10029/','http://www.361ok.com/jingdian/10030/','http://www.361ok.com/jingdian/10031/','http://www.361ok.com/jingdian/10032/','http://www.361ok.com/jingdian/10033/','http://www.361ok.com/jingdian/10034/','http://www.361ok.com/jingdian/10035/','http://www.361ok.com/jingdian/10036/','http://www.361ok.com/jingdian/10037/','http://www.361ok.com/jingdian/10038/','http://www.361ok.com/jingdian/10039/','http://www.361ok.com/jingdian/10040/','http://www.361ok.com/jingdian/10041/','http://www.361ok.com/jingdian/10042/','http://www.361ok.com/jingdian/10043/']
        self.proviceurl = ['http://www.361ok.com/jingdian/10437/','http://www.361ok.com/jingdian/10438/','http://www.361ok.com/jingdian/10439/','http://www.361ok.com/jingdian/10440/','http://www.361ok.com/jingdian/10441/','http://www.361ok.com/jingdian/10442/','http://www.361ok.com/jingdian/10443/','http://www.361ok.com/jingdian/10444/','http://www.361ok.com/jingdian/10445/','http://www.361ok.com/jingdian/10446/','http://www.361ok.com/jingdian/10447/','http://www.361ok.com/jingdian/10448/','http://www.361ok.com/jingdian/10449/','http://www.361ok.com/jingdian/10450/','http://www.361ok.com/jingdian/10451/','http://www.361ok.com/jingdian/10452/','http://www.361ok.com/jingdian/10453/','http://www.361ok.com/jingdian/10454/','http://www.361ok.com/jingdian/10455/','http://www.361ok.com/jingdian/10456/','http://www.361ok.com/jingdian/10457/','http://www.361ok.com/jingdian/10458/','http://www.361ok.com/jingdian/10459/','http://www.361ok.com/jingdian/10460/','http://www.361ok.com/jingdian/10461/','http://www.361ok.com/jingdian/10462/','http://www.361ok.com/jingdian/10463/','http://www.361ok.com/jingdian/10464/','http://www.361ok.com/jingdian/10465/','http://www.361ok.com/jingdian/10466/','http://www.361ok.com/jingdian/10467/','http://www.361ok.com/jingdian/10468/','http://www.361ok.com/jingdian/10469/','http://www.361ok.com/jingdian/10470/','http://www.361ok.com/jingdian/10471/','http://www.361ok.com/jingdian/10472/','http://www.361ok.com/jingdian/10473/','http://www.361ok.com/jingdian/10474/','http://www.361ok.com/jingdian/10475/','http://www.361ok.com/jingdian/10476/','http://www.361ok.com/jingdian/10477/','http://www.361ok.com/jingdian/10478/','http://www.361ok.com/jingdian/10479/','http://www.361ok.com/jingdian/10480/','http://www.361ok.com/jingdian/10481/','http://www.361ok.com/jingdian/10482/','http://www.361ok.com/jingdian/10483/','http://www.361ok.com/jingdian/10484/','http://www.361ok.com/jingdian/10485/','http://www.361ok.com/jingdian/10486/','http://www.361ok.com/jingdian/10487/','http://www.361ok.com/jingdian/10488/','http://www.361ok.com/jingdian/10489/','http://www.361ok.com/jingdian/10490/','http://www.361ok.com/jingdian/10491/','http://www.361ok.com/jingdian/10492/','http://www.361ok.com/jingdian/10493/','http://www.361ok.com/jingdian/10494/','http://www.361ok.com/jingdian/10495/','http://www.361ok.com/jingdian/10496/','http://www.361ok.com/jingdian/10497/','http://www.361ok.com/jingdian/10498/','http://www.361ok.com/jingdian/10475/','http://www.361ok.com/jingdian/10476/','http://www.361ok.com/jingdian/10477/','http://www.361ok.com/jingdian/10478/','http://www.361ok.com/jingdian/10479/','http://www.361ok.com/jingdian/10480/','http://www.361ok.com/jingdian/10481/','http://www.361ok.com/jingdian/10482/','http://www.361ok.com/jingdian/10483/','http://www.361ok.com/jingdian/10484/','http://www.361ok.com/jingdian/10485/','http://www.361ok.com/jingdian/10486/','http://www.361ok.com/jingdian/10487/','http://www.361ok.com/jingdian/10488/','http://www.361ok.com/jingdian/10489/','http://www.361ok.com/jingdian/10490/','http://www.361ok.com/jingdian/10491/','http://www.361ok.com/jingdian/10492/','http://www.361ok.com/jingdian/10493/','http://www.361ok.com/jingdian/10494/','http://www.361ok.com/jingdian/10495/','http://www.361ok.com/jingdian/10496/','http://www.361ok.com/jingdian/10497/','http://www.361ok.com/jingdian/10498/','http://www.361ok.com/jingdian/10475/','http://www.361ok.com/jingdian/10476/','http://www.361ok.com/jingdian/10477/','http://www.361ok.com/jingdian/10478/','http://www.361ok.com/jingdian/10479/','http://www.361ok.com/jingdian/10480/','http://www.361ok.com/jingdian/10481/','http://www.361ok.com/jingdian/10482/','http://www.361ok.com/jingdian/10483/','http://www.361ok.com/jingdian/10484/','http://www.361ok.com/jingdian/10485/','http://www.361ok.com/jingdian/10486/','http://www.361ok.com/jingdian/10487/','http://www.361ok.com/jingdian/10488/','http://www.361ok.com/jingdian/10489/','http://www.361ok.com/jingdian/10490/','http://www.361ok.com/jingdian/10491/','http://www.361ok.com/jingdian/10492/','http://www.361ok.com/jingdian/10493/','http://www.361ok.com/jingdian/10494/','http://www.361ok.com/jingdian/10495/','http://www.361ok.com/jingdian/10496/','http://www.361ok.com/jingdian/10497/','http://www.361ok.com/jingdian/10498/','http://www.361ok.com/jingdian/10475/','http://www.361ok.com/jingdian/10476/','http://www.361ok.com/jingdian/10477/','http://www.361ok.com/jingdian/10478/','http://www.361ok.com/jingdian/10479/','http://www.361ok.com/jingdian/10480/','http://www.361ok.com/jingdian/10481/','http://www.361ok.com/jingdian/10482/','http://www.361ok.com/jingdian/10483/','http://www.361ok.com/jingdian/10484/','http://www.361ok.com/jingdian/10485/','http://www.361ok.com/jingdian/10486/','http://www.361ok.com/jingdian/10487/','http://www.361ok.com/jingdian/10488/','http://www.361ok.com/jingdian/10489/','http://www.361ok.com/jingdian/10490/','http://www.361ok.com/jingdian/10491/','http://www.361ok.com/jingdian/10492/','http://www.361ok.com/jingdian/10493/','http://www.361ok.com/jingdian/10494/','http://www.361ok.com/jingdian/10495/','http://www.361ok.com/jingdian/10496/','http://www.361ok.com/jingdian/10497/','http://www.361ok.com/jingdian/10498/']
        # self.proviceurl = ['http://www.361ok.com/jingdian/10437/']

    def start_requests(self):
        for url in self.proviceurl:
            yield Request(url=url, callback=self.parseProvince)

    def parseProvince(self, response):
        soup = BeautifulSoup(response.body.decode('gb18030'), 'lxml')
        all = soup.find_all(id="all")
        # 省份找不到all标签，直辖市才有
        html = response.body.decode('gb18030')
        if all:
            soup = BeautifulSoup(html, 'lxml')
            lists = soup.find_all(class_="scenic-list")[0].find_all('li')
            for li in lists:
                try:
                    url = li.a['href']
                    yield Request(url=url, callback=self.parseVisiter)
                except Exception as e:
                    with open('error.txt', 'a+') as f:
                        f.write(str(e)+'\n')
                    continue
        else:
            soup = BeautifulSoup(html, 'lxml')
            lists = soup.find_all(class_="city-list")[0].find_all('li')
            for li in lists:
                url = li.a['href']
                yield Request(url=url, callback=self.parseProvince)



    # def getVisitUrl(self, html):
    #     soup = BeautifulSoup(html, 'lxml')
    #     lists = soup.find_all(class_="scenic-list")[0].find_all('li')
    #     for li in lists:
    #         url = li.a['href']
    #         yield Request(url=url, callback=self.parseVisiter)
    #
    # def getCityUrl(self, html):
    #     soup = BeautifulSoup(html, 'lxml')
    #     lists = soup.find_all(class_="city-list")[0].find_all('li')
    #     print 3
    #     for li in lists:
    #         url = li.a['href']
    #         yield Request(url=url, callback=self.parseProvince)

    def parseVisiter(self, response):
        soup = BeautifulSoup(response.body.decode('gb18030'), 'lxml')
        info = soup.find(class_="txt").get_text()
        name = soup.find(class_="sleft").h1.get_text()
        addr = soup.find(class_="sleft").p.get_text().encode('utf-8')
        if not addr.replace('地址：', ''):
            addr += soup.find(class_="crumbs").find_all('a')[-1].get_text().encode('utf-8')
        item = VisiterItem()
        item['name'] = name
        item['info'] = info
        item['addr'] = addr
        yield item



