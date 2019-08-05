import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import unidecode

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
		# Loop through each track
		for track in response.css('td.track-info'):
			# Album name is contained in page title before ' -'
			albumName = unidecode.unidecode(response.css('title::text').get().split(' -')[0])
			trackTitle = unidecode.unidecode(track.css('span.track-title::text').get())
			trackArtist = unidecode.unidecode(track.css('span.track-artist::text').get())
			if (albumName is not None and trackTitle is not None and trackArtist is not None):
				yield {'albumName': albumName, 'Title': trackTitle, 'Artist': trackArtist}