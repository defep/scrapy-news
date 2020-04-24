# -*- coding: utf-8 -*-
import scrapy
from items import Article


class PerfilSpider(scrapy.Spider):
    name = 'perfil'
    allowed_domains = ['perfil.com']
    start_urls = ['https://www.perfil.com//']

    def parse(self, response):
        for el in response.xpath('//article'):
            article = Article()
            title = el.xpath('.//h2/a/text()').get(default='').strip()
            url = el.xpath('.//h2/a/@href').get()
            author = el.xpath('.//span[contains(@class, "autorNota")]/text()').get(default=None)

            if title:
                article['title'] = title
                article['url'] = url
                article['author'] = author
                yield article
