'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 28/07/2020 11:55 PM
@Software: PyCharm
@File    : run_taobao_spider.py
@Email   : huangsiyuan924@gmail.com
'''


from scrapy.cmdline import execute

execute("scrapy crawl taobao".split())