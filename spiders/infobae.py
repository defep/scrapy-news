# -*- coding: utf-8 -*-
import scrapy
from items import Article


class InfobaeSpider(scrapy.Spider):
    name = 'infobaespider'
    start_urls = ['https://www.infobae.com']

    def parse(self, response):
        for el in response.css('.headline'):
            url = response.url + el.css('a').attrib['href']

            article = Article()
            article['title'] = el.css('a::text').get().strip()
            article['url'] = url
            yield article
