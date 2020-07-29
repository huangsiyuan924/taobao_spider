'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 29/07/2020 5:25 PM
@Software: PyCharm
@File    : mysqlUtil.py
@Email   : huangsiyuan924@gmail.com
'''
import json

import pymysql


class MysqlHelper():

    def __init__(self):
        # 连接MySQL
        self.db = pymysql.connect("localhost", "root", "asdasdasd", "test")
        # 创建cursor对象
        self.cursor = self.db.cursor()

        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS taobao_spider(
                            baby_id INT PRIMARY KEY,
                            seller_id INT,
                            baby_url VARCHAR(500),
                            baby_title VARCHAR(100),
                            shop_name VARCHAR(30),
                            shop_url VARCHAR(200),
                            baby_currency_price DECIMAL(10, 2),
                            detail_score FLOAT(2, 1),
                            service_score FLOAT(2, 1),
                            logistics_score FLOAT(2, 1),
                            baby_origin_price DECIMAL(10, 2),
                            sold_total_count INT,
                            confirm_goods_count INT,
                            total_comments_count INT,
                            good_comments_count INT,
                            normal_comments_count INT,
                            bad_comments_count INT
)''')

    def insert_taobao_spider(self,
                         baby_id,
                         seller_id,
                         baby_url,
                         baby_title,
                         shop_name,
                         shop_url,
                         baby_currency_price,
                         detail_score,
                         service_score,
                         logistics_score,
                         baby_origin_price,
                         sold_total_count,
                         confirm_goods_count,
                         total_comments_count,
                         good_comments_count,
                         normal_comments_count,
                         bad_comments_count):
        sql = "INSERT INTO taobao_spider(baby_id,seller_id,baby_url,baby_title, shop_name, shop_url, baby_currency_price, detail_score, service_score, logistics_score, baby_origin_price, sold_total_count, confirm_goods_count,total_comments_count,good_comments_count,normal_comments_count, bad_comments_count) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' '%s', '%s', '%s', '%s', '%s', '%s', '%s',)" % (
        baby_id, seller_id, baby_url, baby_title, shop_name, shop_url, baby_currency_price, detail_score, service_score,
        logistics_score, baby_origin_price, sold_total_count, confirm_goods_count, total_comments_count,
        good_comments_count, normal_comments_count, bad_comments_count)
        self.cursor.execute(sql)
        self.db.commit()

    def insert_base_taobao_spider(self,baby_url, baby_id,baby_title,baby_price,pay_num,detail_score):
        sql = "INSERT INTO taobao_spider(baby_url, baby_id,baby_title,baby_price,pay_num,detail_score) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (baby_url, baby_id,baby_title,baby_price,pay_num,detail_score)
        self.cursor.execute(sql)
        self.db.commit()

    def close(self):
        self.db.close()

class MysqlBaseHelper():

    def __init__(self):
        # 连接MySQL
        self.db = pymysql.connect("localhost", "root", "asdasdasd", "test")
        # 创建cursor对象
        self.cursor = self.db.cursor()

        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS taobao_base_spider(
                            baby_id BIGINT PRIMARY KEY,
                            baby_title VARCHAR(100),
                            baby_price DECIMAL(10, 2),
                            pay_num INT,
                            detail_score FLOAT(2, 1),
                            baby_url VARCHAR(500)
                )''')

    def insert_base_taobao_spider(self, baby_id, baby_title, baby_price, pay_num, detail_score, baby_url):
            sql = "INSERT INTO taobao_base_spider(baby_id,baby_title,baby_price,pay_num,detail_score, baby_url) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (baby_id, baby_title, baby_price, pay_num, detail_score, baby_url)
            print(sql)
            self.cursor.execute(sql)
            self.db.commit()
def test():
    pass
    # helper = MysqlHelper()
    # helper.cursor.execute("SELECT comments_list FROM qsbk")
    # mydata = helper.cursor.fetchall()
    # for i in range(len(mydata)):
    #     datas = json.loads(mydata[i][0], encoding='utf-8', strict=False)
    #     for data in datas:
    #         print(data[0] + ": " + data[1])
    #     print("*" * 40)


if __name__ == '__main__':
    test()
