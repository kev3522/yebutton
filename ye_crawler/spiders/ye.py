import scrapy
import re
import csv


class yeSpider(scrapy.Spider):
	name = "ye"
	allowed_domains = ['lyrics.az']

	def getsongurls(self,response):
		urls = []
		#trs = response.xpath('//div[@class="right-column main-content author-page"]/table/tbody')
		trs = response.xpath('//div[@class="block-content"]//tr')
		for tr in trs:
			url = tr.xpath('./td//@href').extract()
			if len(url) > 0:
				url = 'https://lyrics.az' + url[0]
				urls.append(url)
		return urls

	def scrapesong(self,response):
		lyrics = response.xpath('//p[@id="lyrics"]//text()').extract()
		lyrics = lyrics[0].encode('utf-8')
		lyrics = lyrics.replace("\n\n","\n")
		return response.url, lyrics

	def start_requests(self):
		urls = ['https://lyrics.az/kanye-west/allsongs.html']
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

	def parse(self, response):
		response = response.replace(body=response.body.replace('<br />', '\n'))
		url = response.url
		songlist = []
		lyricslist = []
		if url == 'https://lyrics.az/kanye-west/allsongs.html':
			songs = self.getsongurls(response)
			for song in songs:
				print song
				yield scrapy.Request(url=song, callback=self.parse, dont_filter=False)
		else:
			scraped = self.scrapesong(response)
			with open("songlyrics.csv",'a') as a:
				writer = csv.writer(a, delimiter=",")
				writer.writerow([scraped[0],scraped[1]])



