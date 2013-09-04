# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 04/09/2013

@author: lucas
'''

import requests
from pyquery import PyQuery

class SpiderMan:
    
    urls = ('http://www.uol.com.br',)
    
    #request GET para todas as urls, e retorna o html para o método def
    def get(self):
        try:
            for url in self.urls:
                try:
                    html = requests.get(url).content
                    html = PyQuery(html)
                    self.parse(html)
                except:
                    print ('Erro na requisição da página: ', url)
        except:
            print ("Não foi possíve completar a requisição às páginas")
    
    #parsea as principais notícias dos blogs, retorna os itens parseados
    def parse(self, html):
        try:
            pq = PyQuery(html)
            results = pq('div.moduloChamada > h1 > a')
            for result in results:
                print pq(result).text(), "\n"
        except:
            print ("Não foi possível parsear o HTML")
            
    #método principal que execulta             
    def search(self):
        self.get()

spider = SpiderMan()
spider.search()
