from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist.items import CraigslistItem
import csv

class MySpider(BaseSpider):
  name = "craig"
  allowed_domains = ["craigslist.org"]
  start_urls = ["http://chicago.craigslist.org/search/apa"]

  def parse(self, response):
        HXS = HtmlXPathSelector(response)
        item  = CraigslistItem()
        item['cost'] = HXS.select('//span[@class = "price"]/text()').extract()
        item['location'] = HXS.select('//span[@class = "pnr"]/small/text()').extract()

        yield item