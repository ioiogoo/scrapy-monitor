# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class VisiterPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='qwer', charset='utf8', db='visit')
        self.cur = self.conn.cursor()
        self.sql = 'insert into test(name, addr, info) VALUES(%s,%s,%s)'

    def process_item(self, item, spider):
        values = [item.get('name'), item.get('addr'), item.get('info')]
        try:
            self.cur.execute(self.sql, values)
            self.conn.commit()
        except Exception as e:
            print e

        return item
