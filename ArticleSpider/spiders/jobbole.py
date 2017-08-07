# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112085/']

    def parse(self, response):
        title=response.xpath('//*[@id="post-112085"]/div[1]/h1/text()')
        create_date=response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip()
        praise_numbers=int(response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0])
        fav_numbers = int(response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0])
        match_re=re.match(".*(\d+).*",fav_numbers)
        if match_re:
            fav_numbers=match_re.group(1)
        comment_nums = response.xpath('//a[@href="#article-comment"]/span').extract()
        match_re = re.match(".*(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)
        content=response.xpath("//div[@class='entry']").extract()
        pass
