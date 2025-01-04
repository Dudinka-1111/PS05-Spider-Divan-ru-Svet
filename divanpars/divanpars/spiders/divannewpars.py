import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = 'divannewpars'
    allowed_domains = ['https://divan.ru']
    start_urls = ['https://www.divan.ru/perm/category/lyustry']

    def parse(self, response):
        lamps = response.css('div.LlPhw')
        for lamp in lamps:
            yield {
                'name' : lamp.css('div.lsooF span::text').get(),
                'price' : lamp.css('div.pY3d2 span::text').get(),
                'url' : lamp.css('a').attrib['href']}
