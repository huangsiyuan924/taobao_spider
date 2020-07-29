# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from taobao_spider.mysqlUtil import MysqlHelper


class TaobaoSpiderPipeline(object):

    def __init__(self):
        self.helper = MysqlHelper()

    def process_item(self, item, spider):
        baby_id = item["baby_id"]
        seller_id = item["seller_id"]
        baby_url = item["baby_url"]
        baby_title = item["baby_title"]
        shop_name = item["shop_name"]
        shop_url = item["shop_url"]
        baby_currency_price = item["baby_currency_price"]
        detail_score = item["detail_score"]
        service_score = item["service_score"]
        logistics_score = item["logistics_score"]
        baby_origin_price = item["baby_origin_price"]
        sold_total_count = item["sold_total_count"]
        confirm_goods_count = item["confirm_goods_count"]
        total_comments_count = item["total_comments_count"]
        good_comments_count = item["good_comments"]
        normal_comments_count = item["normal_comments"]
        bad_comments_count = item["bad_comments"]

        self.helper.insert_js_spider(baby_id, seller_id, baby_url, baby_title, shop_name, shop_url, baby_currency_price, detail_score, service_score,logistics_score, baby_origin_price, sold_total_count, confirm_goods_count, total_comments_count,good_comments_count, normal_comments_count, bad_comments_count)
        return item