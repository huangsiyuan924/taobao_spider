# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    baby_id = scrapy.Field()
    seller_id = scrapy.Field()
    baby_url = scrapy.Field()
    baby_title = scrapy.Field()
    shop_name = scrapy.Field()
    shop_url = scrapy.Field()
    baby_currency_price = scrapy.Field()
    detail_score = scrapy.Field()
    service_score = scrapy.Field()
    logistics_score = scrapy.Field()
    baby_origin_price = scrapy.Field()
    sold_total_count = scrapy.Field()
    confirm_goods_count = scrapy.Field()
    total_comments_count = scrapy.Field()
    good_comments_count = scrapy.Field()
    normal_comments_count = scrapy.Field()
    bad_comments_count = scrapy.Field()