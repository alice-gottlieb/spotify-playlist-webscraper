import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

class TimeLifeAutoCrawler(CrawlSpider):
	r'''Crawl from the music page and parse all products.
	
	Attributes:
	name -- TimeLifeCrawlSpider
	start_urls -- time life music page
	rules -- defines rules which select only album sites
	'''
	
	name = 'TimeLifeCrawlSpider'
	allowed_domains = ['timelife.com']
	start_urls = ['https://timelife.com/music']
	
	# Only collect links that include 'product', which denotes a link to an album
	rules = (Rule(LinkExtractor(allow=('products/', )), callback='albumParse'),)

	def albumParse(self, response):
		yield {'link': response.url}