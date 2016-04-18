# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader
from tutorial.items import ArticleItem
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class EndaosiSpider(CrawlSpider):
    name = "endaosi"
    allowed_domains = ["blog.endaosi.com"]
    start_urls = (
        'https://blog.endaosi.com/',
    )
    rules = [
        Rule(LinkExtractor(allow=(r'https://blog.endaosi.com/page/\d/')), callback='parse'),
        Rule(LinkExtractor(allow=(r'https://blog.endaosi.com/.*?/.*?.html')), callback='parse_item'),
    ]

    def parse_item(self, response):
        article = ItemLoader(item=ArticleItem(), response=response)
        # article.add_xpath('title', '//title/text()')
        article.add_value('title', response.xpath('//title/text()')[0].extract())
        return article.load_item()


class EndaosiArticleSpider(scrapy.Spider):
    def parse(self, response):
        pass
