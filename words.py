import scrapy


class DudenSpider(scrapy.Spider):
    name = "duden"
    start_urls = ["http://www.duden.de/definition"]

    def parse(self, response):
        for href in response.css('div.two-cols li a[href*=definition]::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url)

        for href in response.css('div.two-cols li a[href*=rechtschreibung]::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_word)


    def parse_word(self, response):
        word = response.css('#breadcrumb em::text').extract_first()[2:]
        audio = response.css('#content a.audio::attr(href)').extract_first()

        if not audio is None:
            yield {
                'word': word,
                'audio': audio
            }


