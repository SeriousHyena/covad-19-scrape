# the github repo for project is:
# https://github.com/SeriousHyena/covad-19-scrape/blob/master/covad19/spiders/covad_spider.py

import scrapy
from ..items import Covad19Item
    


class CovadSpider(scrapy.Spider):
    name = 'covad'
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        
        items = Covad19Item()
        all_countries = response.css('tbody > tr > td::text').extract()
        foo = []
        #counter = 0

        for item in all_countries[60:-8]:

            case_item = item 
            foo.append(case_item)
            

            items['foo'] = foo
            
            
            if len(foo) > 8:
       
                yield items
                foo.clear()

CovadSpider()






          
            
            
            

    



            
