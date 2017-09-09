# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']


    def parse(self, response):

        author_urls = response.css("span > a::attr(href)").extract()
        for url in author_urls:
            abs_url = response.urljoin(url)
            yield scrapy.Request(url = abs_url, callback = self.parse_details)
            
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url:
            next_page_abs_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = next_page_abs_url, callback = self.parse)


    def parse_details(self, response):
        author_info = {
            "Author Name": response.css("div.author-details>h3.author-title::text").extract_first(),
            "Author Born Date": response.css("div.author-details>p>span.author-born-date::text").extract_first(),
            "Author Born location": response.css("div.author-details>p>span.author-born-location::text").extract_first(),
            "author Description" : response.css("div.author-description").extract_first()
        }
        yield author_info