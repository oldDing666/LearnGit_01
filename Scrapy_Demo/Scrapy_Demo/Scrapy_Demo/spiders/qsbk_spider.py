# -*- coding: utf-8 -*-
import scrapy
from Scrapy_Demo.items import ScrapyDemoItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    # 这是一个列表，可以添加多个，但是一般只写一个就够了
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        # print('*'*30)
        # print(type(response))
        # print('*'*30)
        duanzidivs = response.xpath("//div[@class='col1 old-style-col1']/div")
        # print(duanzidivs)
        for duanzidiv in duanzidivs:
            # print(duanzidiv)
            duanzi_author = duanzidiv.xpath(".//h2/text()").get().strip()
            print(duanzi_author)
            duanzi_content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            duanzi_content = "".join(duanzi_content).strip()
            print(duanzi_content)
            item = ScrapyDemoItem(author=duanzi_author, content=duanzi_content)
            yield item

        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        next_url = "https://www.qiushibaike.com" + next_url

        if not next_url:
            return
        else:
            yield scrapy.Request(next_url, callback=self.parse)
