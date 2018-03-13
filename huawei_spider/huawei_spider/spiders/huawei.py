

from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from huawei_spider.items import HuaweiSpiderItem


class AppStoreSpider(CrawlSpider):
    name = 'huawei'

    allowed_domains = ["app.hicloud.com"]
    start_urls =['http://app.hicloud.com/']
    rules = [
        Rule(LinkExtractor(allow='app/C\d+'),callback='parse_items')
    ]

    def parse_items(self,response):
        item = HuaweiSpiderItem()

        item['appName'] = response.xpath("//p/span[@class='title']/text()").extract()
        item['appDesc'] = response.xpath("//div[@id='app_strdesc']/text()").extract()
        item['url'] = response.url



        yield item

