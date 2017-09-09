# -*- coding: utf-8 -*-
import scrapy
import json

class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	allowed_domains = ['toscrape.com']
	api_url = "http://quotes.toscrape.com/api/quotes?page={}"
	start_urls = [api_url.format(1)]


	def parse(self, response):
		data = response.text
		data = json.loads(data)
		quotes = data['quotes']
		for quote in quotes:
			item = {
				"Quote": quote['text'],
				"Author": quote['author']['name'],
				"Tags": quote['tags']
			}
			yield item

		next_page = int(data['page']) + 1
		next_page_url = self.api_url.format(next_page)
		if bool(data['has_next']):
		    yield scrapy.Request(url = next_page_url, callback = self.parse)
