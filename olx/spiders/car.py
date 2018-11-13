import scrapy
from datetime import datetime
from datetime import timedelta
import pytz


class OlxCar(scrapy.Spider):
    name = "olx_car"

    page_total = raw_input("Jumlah Halaman : ")
    if not page_total:
        page_total = 1

    start_urls = ['https://www.olx.co.id/mobil/bekas/semarang-kota/?page={}'.format(
        x) for x in xrange(1, int(page_total) + 1)]

    def parse(self, response):
        # Follow links to car detail
        for data in response.css('tr.cursor'):
            href = data.css('a.link.linkWithHash::attr(href)').extract_first()
            phone = data.css('button.phone::attr(data-phone)').extract_first()
            date = data.css('td.rel.tcenter > p::text').extract_first().strip()
            # phone = 123
            yield response.follow(href, self.parse_detail, meta={'phone': phone, 'date': date})

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

        def to_float(value):
            value = value.replace(".", "")
            return float(value)

        def extract_specification():
            result = {}
            for data in response.css('ul.spesifikasi > li'):
                title = data.css('span::text').extract_first().strip()
                if data.css('a'):
                    result[title] = data.css(
                        'a::text').extract_first().replace(":", "")
                else:
                    result[title] = data.css('::text')[2].extract().replace(
                        "\t", "").replace("\n", "")

            return result

        def convert_date(value):
            now = datetime.now(pytz.timezone('Asia/Jakarta'))
            month = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
                     "Jul", "Agu", "Sep", "Okt", "Nop", "Des"]

            if ":" in value:
                return now
            elif value == "kemarin":
                return now - timedelta(days=1)
            else:
                value = value.split(" ")
                return datetime(now.year, month.index(value[2])+1, int(value[0]))

        yield dict({
            'Name': extract_first('h1.brkword::text'),
            'Owner': extract_first('div.userbox > p > a > span.brkword::text'),
            'Price': to_float(extract_first('div.pricelabel > strong > span::text')),
            'Phone': response.meta['phone'],
            'Location': extract_first('span.icon.markerloc + span > strong > a::text'),
            'Show': to_float(extract_first('#offerbottombar > .clr.rel + div.pdingtop10 > strong::text')),
            'Date': convert_date(response.meta['date']),
        }, **extract_specification())
