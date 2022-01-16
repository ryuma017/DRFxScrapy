import scrapy
from bs4 import BeautifulSoup

from crawler.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        try:
            text = ''
            author = ''
            tags = ''

            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all(name='div', attrs={'class': 'quote'})

            crawling_url = response.url
            print(f'crawling: {crawling_url}')

            for quote in quotes:
                if quote.select('span.text'):
                    text = quote.select('span.text')[0].get_text(strip=True)[1:-1] #<-- [1:-1]で両端の''を削除

                if quote.select('small.author'):
                    author = quote.select('small.author')[0].get_text(strip=True)

                if quote.select('a.tag'):
                    tags_ResultSet = quote.select('a.tag')
                    tags_text_list = [tags_ResultSet[i].get_text() for i in range(len(tags_ResultSet))]
                    tags = ', '.join(tags_text_list)

                yield QuoteItem(
                    text=text,
                    author=author,
                    tags=tags
                )

            next_page = soup.find(name='li', attrs={'class': 'next'}).a.get('href')
            if next_page is not None:
                # URLを絶対パスに変換
                next_page = response.urljoin(next_page)

                yield scrapy.Request(next_page, callback=self.parse)

        except Exception as e:
            http_status_code = response.status
            print(f'Http Status Code: {http_status_code}')
            print(f'ERROR: {e}')

        else:
            print('Successfully completed ')
