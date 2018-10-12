import scrapy
#scrapy crawl speakers -o speakers.json

class SpeakersSpider(scrapy.Spider):
    name = "speakers"
    start_urls = [
        'https://www.israelblockchainsummit.com/',
    ]
    def parse(self, response):
        for speaker in response.xpath('//div[@class="speakers_hover"]'):
            yield {
                'name': speaker.xpath('./h3/text()').extract_first(),
                'title': speaker.xpath('./div/h5/text()').extract_first(),
                'linkedin': speaker.xpath('./div//@href').extract_first(),
                'link': speaker.xpath('.//@href')[-1].extract()
            }
