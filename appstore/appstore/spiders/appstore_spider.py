
from appstore.items import AppstoreItem
from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

class AppStoreSpider(CrawlSpider):
    name = 'appstore'

    allowed_domains = ["app.hicloud.com"]
    start_urls =['http://app.hicloud.com/']
    rules = [
        Rule(LinkExtractor(allow='app/C\d+'),callback='parse_items')
    ]

    def parse_items(self,response):
        item = AppstoreItem()

        name = response.xpath("//p/span[@class='title']").extract()

        # print ''.join(name).decode('utf-8')

        yield item

