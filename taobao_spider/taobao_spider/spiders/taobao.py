# -*- coding: utf-8 -*-
import scrapy


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://re.taobao.com/search?keyword=%E9%92%88%E7%BB%87%E8%BF%9E%E8%A1%A3%E8%A3%99&page=0']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.page = 0

    def parse(self, response):
        # 下一页的页数
        self.page += 1
        # 下一页的url
        next_page = 'https://re.taobao.com/search?keyword=%E9%92%88%E7%BB%87%E8%BF%9E%E8%A1%A3%E8%A3%99&page=' + str(self.page)
        # # 宝贝标题
        # title = response.xpath('//span[@class="title"]//text()').extract()
        # 宝贝详情url
        baby_url_list = response.xpath('//div[@class="item"]/a/@href').extract()
        price_list = response.xpath('//span[@class="pricedetail"]/strong/text()').extract()
        print(price_list)
        for baby_url in baby_url_list:
            yield scrapy.Request(
                url=baby_url,
                dont_filter=True,
                callback=self.parse_baby_detail
            )

    def parse_baby_detail(self, response):
        # 宝贝标题
        baby_title = response.xpath('//h3[@class="tb-main-title"]/text()').extract_first().strip()
        print(baby_title)
        # 店家名字
        shop_name = response.xpath('//div[@class="tb-shop-name"]//a/text()').extract_first().strip()
        print(shop_name)
        baby_price = response.xpath('//em[@id="J_PromoPriceNum"]/text()').extract()
        print(baby_price)