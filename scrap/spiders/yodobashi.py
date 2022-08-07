import logging
import scrapy


class YodobashiSpider(scrapy.Spider):
    name = 'yodobashi'
    allowed_domains = ['www.yodobashi.com']
    start_urls = ['https://www.yodobashi.com/category/19531/11970/34646/']

    def parse(self, response):
        logging.info(response.url)
        products = response.xpath('//div[contains(@class, "productListTile")]')

        for product in products:
            # productにはセレクターオブジェクトが格納されている
            # セレクターオブジェクトに対してxpathを記述する場合、xpathの先頭にドットをつける必要がある（cssセレクターで指定する場合は必要なし）
            
            maker = product.xpath('.//div[contains(@class, "pName")]/p/text()').get()
            name = product.xpath('.//div[contains(@class, "pName")]/p[2]/text()').get()
            price = product.xpath('.//span[@class="productPrice"]/text()').get()
            yield {
                'maker': maker,
                'name': name,
                'price': price
            }
        # 最初のページで商品の情報を取得し、「次のページ」のリンクを辿って、次のページの情報を取得
        next_page = response.xpath('//a[@class="next"]/@href').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
