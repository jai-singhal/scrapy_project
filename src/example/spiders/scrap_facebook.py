# -*- coding: utf-8 -*-
import scrapy
import json

class FacebookSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['https://www.facebook.com/']
    login_url = "https://www.facebook.com/"
    start_urls = [login_url,]

    def parse(self, response):
        data = {
            'username': response.css("input[name='email']::attr(value)").extract_first(),
            'password': response.css("input[name='pass']::attr(value)").extract_first(),
        }
       
        yield scrapy.FormRequest(url=self.login_url, formdata = data, callback = self.parse_data)

  
    def parse_data(self, response):
        self.log(" I just visited" + response.url)
