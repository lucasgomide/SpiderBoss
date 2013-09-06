# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 04/09/2013

@author: lucas
'''

import requests
from pyquery import PyQuery

class SpiderMan:
    
    urls = ('http://www.uol.com.br','http://www.globo.com')
    selectors = ('div.moduloChamada > h1 > a', 'div.destaque .chamada-principal a ')
    
    def encondingUTF_8(self, str):
        try:
            return str.encode("utf-8")
        except Exception as e:
            print ("Impossível mudar a codificação do HTML", e)
            
    def getDominio(self, url):
        try:
            url = url.split('.')
            return url[1].upper()
        except Exception as e:
            print ("Não foi possível parsear a URL " ,e)
            
    #request GET para todas as urls, e retorna o html para o método def
    def get(self):
        try:
            for url in self.urls:
                try:
                    html = requests.get(url).content
                    print "Noticias do(a): ", self.getDominio(url)
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
            for seletor in self.selectors:
                results = pq(seletor)
                for result in results:
                    news = pq(result).text()
                    print "--", self.encondingUTF_8(news)
                
        except Exception as e:
            print ("Não foi possível parsear o HTML " ,e)
            
    #método principal que execulta             
    def search(self):
        self.get()

spider = SpiderMan()
spider.search()
