# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        self.log(" I just visited" + response.url)
        for quote in response.css("div.quote"):
            item = {
                "Quote": quote.css("span.text::text").extract_first(),
                "Author": quote.css("small.author::text").extract_first(),
                "author": quote.css("a.tag::text").extract()
            }
            yield item

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url:
            next_page_abs_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = next_page_abs_url, callback = self.parse) 