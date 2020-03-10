# the github repo for project is:
# https://github.com/SeriousHyena/covad-19-scrape/blob/master/covad19/spiders/covad_spider.py

import scrapy
from ..items import Covad19Item

class CovadSpider(scrapy.Spider):
    name = 'covad'
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        items = Covad19Item()
        all_countries = response.css('td::text').extract()
        case_list = []
        

        for item in all_countries:
            case_item = item
            case_list.append(case_item)
            

            items['case_item'] = case_item

            yield items



            
