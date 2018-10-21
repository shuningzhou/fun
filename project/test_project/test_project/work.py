import scrapy
from scrapy.utils.project import get_project_settings
import pandas as pd
import os
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner

settings = get_project_settings()

df = pd.read_csv("dow.csv")
df2 = pd.read_csv("nasdaq.csv")

runner = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl():
    count = 0
    for index, row in df.iterrows():
        symbol = row["Symbol"]
        dir = "./../../DATA/" +  symbol
        if not os.path.exists(dir):
            print "Making directory for " + symbol
            os.makedirs(dir)

        print "Crawling data for " + symbol + " ..."
        yield runner.crawl("stock", stock_name=symbol)
        count = count + 1
        print ('Crawled ', count, ' stocks')

    for index, row in df2.iterrows():
        symbol = row["Symbol"]
    
        dir = "./../../DATA/" +  symbol
        if not os.path.exists(dir):
            print "Making directory for " + symbol
            os.makedirs(dir)
    
        print "Crawling data for " + symbol + " ..."
        yield runner.crawl("stock", stock_name=symbol)
        count = count + 1
        print ('Crawled ', count, ' stocks')

    reactor.stop()

crawl()
reactor.run()



