import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()