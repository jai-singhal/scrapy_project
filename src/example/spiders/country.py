# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ExampleItem

class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/index/'),  follow=True),
        Rule(LinkExtractor(allow=r'/view/'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = ExampleItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
