# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from apk_parse.items import ApkParseItem

class ApkSpider(CrawlSpider):
    name = "apk"
    allow_domains = ["http://app.hicloud.com"]
    start_urls = ["http://app.hicloud.com/app/C33455"]

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表
    pagelink = LinkExtractor(allow=("/app/C\d+"))

    rules = [
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(pagelink, callback="parseApk", follow=True)
    ]

    def parseApk(self, response):
        item = ApkParseItem()
        item['name'] = response.xpath("//p/span[@class='title']/text()").extract()
        item['url'] = response.url

        yield item
