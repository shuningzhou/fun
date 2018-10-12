# -*- coding: utf-8 -*-
import scrapy
from test_project.items import TestProjectItem
import datetime

# getting sector, industry, country
# response.xpath('//*[@class="fullview-title"]/tr[3]/td/a/text()').extract()
# scrapy crawl yahoo -a stock_name="snd"

class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    base_url = 'https://finviz.com/quote.ashx?t='
    allowed_domains = ['www.finviz.com']
    FILE_DIR = '/Users/shuningzhou/Desktop/scrapy/DATA/'

    def __init__(self, stock_name):
        self.start_urls = [self.base_url + stock_name]
        self.item = TestProjectItem()
        self.file_name = self.FILE_DIR + stock_name + '.csv'
        self.ratings_file_name = self.FILE_DIR + stock_name + "_ratings.csv"

    def set_value(self, name, value):

        if name == 'Market Cap' :
            self.item['market_cap'] = value
        elif name == 'Shs Float' :
            self.item['shs_float'] = value
        elif name == 'Insider Trans' :
            self.item['insider_trans'] = value
        elif name == 'Shs Outstand' :
            self.item['shs_outstand'] = value
        elif name == 'EPS (ttm)' :
            self.item['eps'] = value
        elif name == 'Insider Own' :
            self.item['insider_own'] = value
        elif name == 'Forward P/E' :
            self.item['f_p_e'] = value
        elif name == 'P/E' :
            self.item['p_e'] = value
        elif name == 'Dividend' :
            self.item['dividend'] = value
        elif name == 'ROE' :
            self.item['roe'] = value
        elif name == 'P/C' :
            self.item['p_c'] = value
        elif name == 'Target Price' :
            self.item['target_price'] = value
        elif name == 'ROA' :
            self.item['roa'] = value
        elif name == 'P/B' :
            self.item['p_b'] = value
        elif name == 'Short Ratio' :
            self.item['short_ratio'] = value
        elif name == 'Inst Trans' :
            self.item['inst_trans'] = value
        elif name == 'P/S' :
            self.item['p_s'] = value
        elif name == 'Sales' :
            self.item['sales'] = value
        elif name == 'Short Float' :
            self.item['short_float'] = value
        elif name == 'Inst Own' :
            self.item['inst_own'] = value
        elif name == 'PEG' :
            self.item['peg'] = value
        elif name == 'Gross Margin' :
            self.item['gross_margin'] = value
        elif name == 'Quick Ratio' :
            self.item['quick_ratio'] = value
        elif name == 'Dividend %' :
            self.item['dividend_percent'] = value
        elif name == 'ROI' :
            self.item['roi'] = value
        elif name == 'Income' :
            self.item['income'] = value
        elif name == 'Change' :
            self.item['change'] = value
        elif name == 'Volume' :
            self.item['volume'] = value
        elif name == 'SMA200' :
            self.item['sma200'] = value
        elif name == 'SMA50' :
            self.item['sma50'] = value
        elif name == 'SMA20' :
            self.item['sma20'] = value
        elif name == 'Recom' :
            self.item['recom'] = value
        elif name == 'Price' :
            self.item['price'] = value
        elif name == 'Avg Volume' :
            self.item['avg_volume'] = value
        elif name == 'Prev Close' :
            self.item['prev_close'] = value
        elif name == 'Profit Margin' :
            self.item['profit_margin'] = value
        elif name == 'EPS Q/Q' :
            self.item['eps_q_to_q'] = value
        elif name == 'Debt/Eq' :
            self.item['debt_eq'] = value
        elif name == 'RSI (14)' :
            self.item['rsi'] = value
        elif name == 'Oper. Margin' :
            self.item['oper_margin'] = value
        elif name == 'Sales Q/Q' :
            self.item['sales_q_to_q'] = value
        elif name == 'Current Ratio' :
            self.item['current_ratio'] = value
        elif name == 'Employees' :
            self.item['employees'] = value
        elif name == '52W Low' :
            self.item['low_y'] = value
        elif name == '52W High' :
            self.item['high_y'] = value

        else :
            print 'PETER: UNKNOWN NAME = ' + name

    def parse(self, response):

        # get stock data
        print '====== GETTING STOCK DATA ======'
        names = response.xpath('//*[@class="table-dark-row"]/*[@class="snapshot-td2-cp"]')
        values = response.xpath('//*[@class="table-dark-row"]/*[@class="snapshot-td2"]')
        name_count = len(names)
        value_count = len(values)

        if name_count == value_count :
            for index in range(0, name_count):
                n = names[index].xpath('text()').extract_first()
                v = values[index].xpath('b/text()').extract_first()

                if v is None:
                    v = values[index].xpath('b/span/text()').extract_first()

                print n
                print v

                if n is None or v is None:
                    continue
                else:
                    self.set_value(n.strip(), v.strip())
        
        # get rating
        print '====== GETTING RATINGS ======'
        ratings = response.xpath('//*[@class="fullview-ratings-inner"]//td')
        RATING_ROWS = 5

        today_value = datetime.datetime.now().strftime("%b-%d-%y")
        print today_value
        today_value = 'Mar-17-17'
        ratings_count = len(ratings)
        new_ratings = []
        for index in range(0, ratings_count):

            print 'INDEX = ', index

            # check date
            if index % RATING_ROWS == 0:
                # get text
                date_value = ratings[index].xpath('text()').extract_first()
                print date_value

                # only get rating for today
                if date_value == today_value:
                    action_value = ratings[index+1].xpath('b/text()').extract_first()
                    name_value = ratings[index+2].xpath('text()').extract_first()
                    rate_value = ratings[index+3].xpath('text()').extract_first()
                    r_d = rate_value.encode('utf-8')
                    r_d = r_d.replace("\xe2\x86\x92", "to")

                    target_value = ratings[index+4].xpath('text()').extract_first()
                    t_d = target_value.encode('utf-8')
                    t_d = t_d.replace("\xe2\x86\x92", "to")
            
                    new_rating = {
                        'date': date_value,
                        'action': action_value,
                        'name': name_value,
                        'rate': r_d,
                        'target': t_d
                    }

                    print new_rating

                    new_ratings.append(new_rating)

        print new_ratings

        result = {
            'item': self.item,
            'new_ratings': new_ratings
        }

        return result
