# -*- coding: utf-8 -*-
import scrapy

class NewsSpider(scrapy.Spider):
    name = 'newsspider'
    start_urls = ['https://www.infobae.com']

    def parse(self, response):
        for title in response.css('.headline'):
            yield {'title': title.css('a::text').get()}
