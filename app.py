import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.infobae import InfobaeSpider


process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'infobae.json'
})

process.crawl(InfobaeSpider)
process.start()