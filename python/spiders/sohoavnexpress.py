import scrapy

class sohoaVnexpressNetSpider(scrapy.Spider):
    name = "sohoa"

    def start_requests(self):
        urls = [
            'https://sohoa.vnexpress.net/tin-tuc/doi-song-so/tap-chi-co-chu-ky-steve-jobs-duoc-ban-gia-50-000-usd-3662652.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_artilce)

    def parse_artilce(self, response):
        artilce = {}
        artilce['title'] = response.xpath('//*[@id="col_sticky"]/h1/text()').extract()[0].encode('utf-8').strip()
        artilce['description'] = response.xpath('//*[@id="col_sticky"]/h2').extract()[0].encode('utf-8').strip()
        artilce['content'] = response.xpath('//*[@id="col_sticky"]/article').extract()[0].encode('utf-8').strip()
        artilce['author'] = response.xpath('//*[@id="col_sticky"]/article/p[5]/strong/text()').extract()[0].encode('utf-8').strip()
        artilce['publish_date'] = response.xpath('//*[@id="col_sticky"]/header/span/text()').extract()[0].encode('utf-8').strip()
        for key, text in artilce.iteritems():
            print "{key}: {text}".format(key = key.upper(), text = text)