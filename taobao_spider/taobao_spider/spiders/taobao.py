# -*- coding: utf-8 -*-
import json

import scrapy

from taobao_spider.items import TaobaoSpiderItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://re.taobao.com/search?keyword=%E9%92%88%E7%BB%87%E8%BF%9E%E8%A1%A3%E8%A3%99&page=0']



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.page = 0
        self.cookies = {
    "cna":"oqM2F/nSZDgCARdiJwMONIc/",
    "_fbp":"fb.1.1590839454714.6573722",
    "thw":"cn",
    "sgcookie":"Evirr6LUhp5dF5Zkj1gsa",
    "tracknick":"%5Cu8FDChaxp",
    "_cc_":"Vq8l%2BKCLiw%3D%3D",
    "enc":"nyJT22t48jW6bvn3u94muepcodD4tXQt%2Fo7KSwjWXcEXEL4KhrtFHZ0jtQpOunv4cFkGfpAJBh%2FfSC9FT%2BP06w%3D%3D",
    "ubn":"p",
    "ucn":"center",
    "miid":"313700271972906312",
    "t":"2e45f0da87b4d1cab80ccc82de23d5fa",
    "mt":"ci%3D-1_0",
    "cookie2":"1f56f94ea0052248d1941c6585358614",
    "v":"0",
    "_m_h5_tk":"f98958d228172f204c05c1048f8ad8e0_1596007630333",
    "_m_h5_tk_enc":"d054af79caf760e71a834fbc538eee95",
    "_samesite_flag_":"true",
    "hng":"US%7Czh-CN%7CUSD%7C840",
    "uc1":"cookie14=UoTV6huM%2FoaaUg%3D%3D",
    "tfstk":"c0aVBgDXlZQ47og1vqgwlQSZbVVAZQDidUlEmkpZyh69RxmcijvtZ_9tafRGCmf..",
    "_tb_token_":"e57e5b3e3e35b",
    "isg":"BPX1qC5mxpX29SPar1OGqwEzBHGvcqmEg99br3cdQG0MTh1APsElVMKHmBL4DsE8",
    "l":"eBPDgdNrQ0kE7B6-BO5Z-urza779BBdfcsPzaNbMiIncC6AFNyptBRtQKyW9QKtRR8XVGPYp46aJ5OeTmFouJyGqndLHRXOi8dkwUFLC.\nreferer: https://item.taobao.com/item.htm?id=620197689807"
}

    def parse(self, response):
        # 下一页的页数
        self.page += 1
        # 下一页的url
        next_page = 'https://re.taobao.com/search?keyword=%E9%92%88%E7%BB%87%E8%BF%9E%E8%A1%A3%E8%A3%99&page=' + str(self.page)
        # # 宝贝标题
        # title = response.xpath('//span[@class="title"]//text()').extract()
        # 宝贝详情url
        baby_url_list = response.xpath('//div[@class="item"]/a/@href').extract()
        baby_price_list = response.xpath('//span[@class="pricedetail"]/strong/text()').extract()
        for baby_url, baby_price in zip(baby_url_list, baby_price_list):
            yield scrapy.Request(
                url=baby_url,
                meta={"baby_price": baby_price},
                dont_filter=True,
                callback=self.parse_page_detail
            )

        yield scrapy.Request(
            url=next_page,
            dont_filter=True,
            callback=self.parse
        )



    def parse_page_detail(self, response):


        # 宝贝id
        baby_id = response.xpath('//div[@id="J_Pine"]/@data-itemid').extract_first()
        #店家id
        seller_id = response.xpath('//div[@id="J_Pine"]/@data-sellerid').extract_first()
        baby_detail_url = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId={}&sellerId={}&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,page,originalPrice,tradeContract&callback=onSibRequestSuccess".format(baby_id, seller_id)


        # 宝贝链接
        baby_url = 'https://item.taobao.com/item.htm?id=' + baby_id
        # 宝贝标题
        baby_title = str(response.xpath('//h3[@class="tb-main-title"]/text()').extract_first()).strip()
        # 店家名字
        shop_name = str(response.xpath('//div[@class="tb-shop-name"]//a/text()').extract_first()).strip()
        # 店家url
        shop_url = "http://shop" + seller_id +".taobao.com"
        # 宝贝现价格
        baby_currency_price = response.meta['baby_price']

        score_list = response.xpath('//dd[@class="tb-rate-higher"]/a/text()').extract()
        # 描述得分
        detail_score = score_list[0].strip()
        # 服务得分
        service_score = score_list[1].strip()
        # 物流得分
        logistics_score = score_list[2].strip()
        yield scrapy.Request(
            url=baby_detail_url,
            meta={
                "baby_id": baby_id,
                "seller_id": seller_id,
                "baby_url": baby_url,
                "baby_title": baby_title,
                "shop_name": shop_name,
                "shop_url": shop_url,
                "baby_currency_price": baby_currency_price,
                "detail_score": detail_score,
                "service_score": service_score,
                "logistics_score": logistics_score,
            },
            dont_filter=True,
            callback=self.parse_baby_detail,
            cookies=self.cookies
        )

    def parse_baby_detail(self, response):
        # print(type(response.body))
        baby_data =json.loads(str(response.body, encoding='utf-8').split("onSibRequestSuccess(")[1].split(")")[0])

        baby_id = response.meta["baby_id"]
        seller_id = response.meta["seller_id"]
        baby_url = response.meta["baby_url"]
        baby_title = response.meta["baby_title"]
        shop_name = response.meta["shop_name"]
        shop_url = response.meta["shop_url"]
        baby_currency_price = response.meta["baby_currency_price"]
        detail_score = response.meta["detail_score"]
        service_score = response.meta["service_score"]
        logistics_score = response.meta["logistics_score"]


        # 宝贝原价格
        baby_origin_price = baby_data["data"]["price"]
        # 总销售数
        sold_total_count = baby_data["data"]["soldQuantity"]["soldTotalCount"]
        # 确认收货数
        confirm_goods_count = baby_data["data"]["soldQuantity"]["confirmGoodsCount"]


        comments_detail_url = "https://rate.taobao.com/detailCommon.htm?auctionNumId="+ baby_id +"&userNumId=" + seller_id

        yield scrapy.Request(
            url=comments_detail_url,
            callback=self.comments_parse,
            meta={
                "baby_id" : baby_id,
                "seller_id" : seller_id,
                "baby_url" : baby_url,
                "baby_title" : baby_title,
                "shop_name" : shop_name,
                "shop_url" : shop_url,
                "baby_currency_price" : baby_currency_price,
                "detail_score" : detail_score,
                "service_score" : service_score,
                "logistics_score" : logistics_score,
                "baby_origin_price" : baby_origin_price,
                "sold_total_count" : sold_total_count,
                "confirm_goods_count" : confirm_goods_count,
            }
        )



    def comments_parse(self, response):
        baby_id = response.meta["baby_id"]
        seller_id = response.meta["seller_id"]
        baby_url = response.meta["baby_url"]
        baby_title = response.meta["baby_title"]
        shop_name = response.meta["shop_name"]
        shop_url = response.meta["shop_url"]
        baby_currency_price = response.meta["baby_currency_price"]
        detail_score = response.meta["detail_score"]
        service_score = response.meta["service_score"]
        logistics_score = response.meta["logistics_score"]
        baby_origin_price = response.meta["baby_origin_price"]
        sold_total_count = response.meta["sold_total_count"]
        confirm_goods_count = response.meta["confirm_goods_count"]
        comments_detail = json.loads(str(response.body, encoding='utf-8').replace("\r\n(", "").replace(")", ""))
        # 累计评论
        total_comments_count = comments_detail["data"]["count"]["total"]
        # 好评数
        good_comments_count = comments_detail["data"]["count"]["good"]
        # 中评数
        normal_comments_count = comments_detail["data"]["count"]["normal"]
        # 差评数
        bad_comments_count = comments_detail["data"]["count"]["bad"]

        item = TaobaoSpiderItem()
        item["baby_id"] = baby_id
        item["seller_id"] = seller_id
        item["baby_url"] = baby_url
        item["baby_title"] = baby_title
        item["shop_name"] = shop_name
        item["shop_url"] = shop_url
        item["baby_currency_price"] = baby_currency_price
        item["detail_score"] = detail_score
        item["service_score"] = service_score
        item["logistics_score"] = logistics_score
        item["baby_origin_price"] = baby_origin_price
        item["sold_total_count"] = sold_total_count
        item["confirm_goods_count"] = confirm_goods_count
        item["total_comments_count"] = total_comments_count
        item["good_comments_count"] = good_comments_count
        item["normal_comments_count"] = normal_comments_count
        item["bad_comments_count"] = bad_comments_count


        yield item
