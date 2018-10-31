import scrapy


class OlxCar(scrapy.Spider):
    name = "olx_car"

    start_urls = ['https://www.olx.co.id/mobil/bekas/semarang-kota/?page={}'.format(x) for x in xrange(1, 51)]

    def parse(self, response):
        # Follow links to car detail
        for data in response.css('tr.cursor'):
            href = data.css('a.link.linkWithHash::attr(href)').extract_first()
            phone = data.css('button.phone::attr(data-phone)').extract_first()
            # phone = 123
            yield response.follow(href, self.parse_detail, meta={'phone':phone})

        # for href in response.css()


    def parse_detail(self, response):
        # Get detail car
        def extract_first(query):
            result = response.css(query).extract_first()
            if result is None:
                return result
                
            return response.css(query).extract_first().strip()

        def extract_all(query):
            return response.css(query).extract()

        def extract_specification():
            result = {}
            for data in response.css('ul.spesifikasi > li').extract():
                title = data.css['span'].extract_first()
                if data.css('a'):
                    result[title] = data.css['a::text'].extract_first()
                else:
                    result[title] = data.css['::text'][2].extract().replace("\t", "").replace("\n", "")

            print result
            return result

        yield {
            'name': extract_first('h1.brkword::text'),
            'owner': extract_first('div.userbox > p > a > span.brkword::text'),
            'price': extract_first('div.pricelabel > strong > span::text'),
            'phone': response.meta['phone'],
            'location': extract_first('span.icon.markerloc + span > strong > a::text'),
        }