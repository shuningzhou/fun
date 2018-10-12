# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os.path
import datetime

class TestProjectPipeline(object):
 
    def process_item(self, result, spider):     

        print 'PETER: PIPLINE'
        print spider.file_name
        print spider.ratings_file_name

        item = result['item']
        new_ratings = result['new_ratings']
        
        print item
        print new_ratings

        # write to ratings file
        if len(new_ratings) > 0:
            if not os.path.isfile(spider.ratings_file_name):
                self.csvwriter = csv.writer(open(spider.ratings_file_name, 'a'))
                self.csvwriter.writerow([                                        
                                            'date',
                                            'action',
                                            'name',
                                            'rate',
                                            'target',
                                        ])
            else: 
                self.csvwriter = csv.writer(open(spider.ratings_file_name, 'a'))

            for rating in new_ratings:
                self.csvwriter.writerow([
                                            rating['date'],
                                            rating['action'],
                                            rating['name'],
                                            rating['rate'],
                                            rating['target'],
                                        ])

        # write to data file
        if not os.path.isfile(spider.file_name):
            self.csvwriter = csv.writer(open(spider.file_name, 'a'))
            self.csvwriter.writerow([
                                        'date',
                                        'time',
                                        'price',
                                        'change',
                                        'volume',
                                        'avg_volume',
                                        'market_cap', 
                                        'income',
                                        'sales',
                                        'p_b',
                                        'p_e',
                                        'f_p_e',
                                        'peg',
                                        'p_c',
                                        'p_s',
                                        'quick_ratio',
                                        'current_ratio',
                                        'debt_eq',
                                        'sma20',
                                        'sma50',
                                        'sma200',
                                        'rsi',
                                        'roa',
                                        'roe',
                                        'roi',
                                        'gross_margin',
                                        'oper_margin',
                                        'profit_margin',
                                        'shs_outstand',
                                        'shs_float',
                                        'short_float',
                                        'short_ratio',
                                        'target_price',
                                        'high_y',
                                        'low_y',

                                        'prev_close',
                                        'eps',
                                        'sales_q_to_q',
                                        'eps_q_to_q',
                                        'insider_own',
                                        'insider_trans',
                                        'inst_own',
                                        'inst_trans',
                                        'dividend',
                                        'dividend_percent',
                                        'employees',
                                        'recom',
                                    ])
        else: 
            self.csvwriter = csv.writer(open(spider.file_name, 'a'))

        d = datetime.datetime.now().strftime("%Y-%m-%d")
        t = datetime.datetime.now().strftime("%H:%M:%S ")
        self.csvwriter.writerow([
                                    d,
                                    t,
                                    item['price'],
                                    item['change'],
                                    item['volume'],
                                    item['avg_volume'],
                                    item['market_cap'], 
                                    item['income'],
                                    item['sales'],
                                    item['p_b'],
                                    item['p_e'],
                                    item['f_p_e'],
                                    item['peg'],
                                    item['p_c'],
                                    item['p_s'],
                                    item['quick_ratio'],
                                    item['current_ratio'],
                                    item['debt_eq'],
                                    item['sma20'],
                                    item['sma50'],
                                    item['sma200'],
                                    item['rsi'],
                                    item['roa'],
                                    item['roe'],
                                    item['roi'],
                                    item['gross_margin'],
                                    item['oper_margin'],
                                    item['profit_margin'],
                                    item['shs_outstand'],
                                    item['shs_float'],
                                    item['short_float'],
                                    item['short_ratio'],
                                    item['target_price'],
                                    item['high_y'],
                                    item['low_y'],
                                    item['prev_close'],
                                    item['eps'],
                                    item['sales_q_to_q'],
                                    item['eps_q_to_q'],
                                    item['insider_own'],
                                    item['insider_trans'],
                                    item['inst_own'],
                                    item['inst_trans'],
                                    item['dividend'],
                                    item['dividend_percent'],
                                    item['employees'],
                                    item['recom'],
                                ])

        return result
