import scrapy


class QiitaTrend1dSpider(scrapy.Spider):
    name = 'qiita_trend_1d'
    allowed_domains = ['qiita.com']
    start_urls = ['https://qiita.com/']

    def parse(self, response):
        # Xpathで取得したい場合
        category = response.xpath('//a[@class="st-NewHeader_mainNavigationItem is-active"]/text()').get()
        titles = response.xpath('//h2/a/text()').getall()
        urls = response.xpath('//h2/a/@href').getall()

        # CSSセレクタで取得したい場合
        # category = response.xpath('a[class="st-NewHeader_mainNavigationItem is-active"]::text').get()
        # titles = response.xpath('h2 > a::text').getall()
        # urls = response.xpath('h2 > a::attr(href)').getall()

        # 戻り値
        # yield：関数の処理を一旦停止し、値を返却する。
        # 記述方法：yield 戻り値
        yield {
            'category': category,
            'titles': titles,
            'urls': urls,
        }


