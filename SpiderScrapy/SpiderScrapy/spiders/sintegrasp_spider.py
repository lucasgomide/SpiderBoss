'''
Created on 06/09/2013

@author: lgomide
'''
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from SpiderScrapy.items import SpiderscrapyItem 

class SintegraSP(BaseSpider):
    name = "sintegrasp"
    allowed_domains = ["pfeserv1.fazenda.sp.gov.br"]
    start_urls = [
                  "http://pfeserv1.fazenda.sp.gov.br/sintegrapfe/consultaSintegraServlet",
                 ]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        results = hxs.select('/html/body/table')
        items = []
        for result in results:
            item = SpiderscrapyItem()
            item['title'] = result.select('/html/body/table/tr/td[2]/table/tr[1]/td/b/font').extract()
            item['desc']  = result.select('/html/body/table/tr/td[2]/table/tr[2]/td/font').extract()
            items.append(item)
        return items
            