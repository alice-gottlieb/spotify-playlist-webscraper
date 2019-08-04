import scrapy
import re

class AlbumSpider(scrapy.Spider):
	r'''Spider to collect each album from main timelife.com/music listing
	
	Attributes:
	name -- 'albumSpider'
	'''

	name = 'albumSpider'
	start_urls = ['https://timelife.com/music']
	
	# def start_requests(self):
		# for url in start_urls:
			# yield url
			
	def parse(self, response):
		r'''Returns every link to a different album on page.'''
		
		# Only collect links that include 'product', which denotes a link to an album
		links = response.xpath('//a[contains(@href, "products")]/@href').getall()
		# Cast to set to remove duplicate links
		links = list(set(links))
		for link in links:
			yield {'link': link}