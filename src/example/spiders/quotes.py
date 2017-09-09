# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        self.log(" I just visited" + response.url)

        yield{
        	'author_name': response.css("small.author::text").extract(),
        	'text': response.css("span.text::text").extract(),
        	'tags': response.css("a.tag::text").extract(),
        }

# quotes = response.css("div.quote")
# quotes_arr = []
# for quote in quotes:
# 	item = {
# 		"Quote": quote.css("span.text::text").extract(),
# 		"Author": quote.css("small.author::text").extract(),
# 		"author": quote.css("a.tag::text").extract()
# 	}
# 	quotes_arr.append(item)

