# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestProjectItem(scrapy.Item):
    # define the fields for your item here like:
        market_cap = scrapy.Field()
        income = scrapy.Field()
        sales = scrapy.Field()
        p_b = scrapy.Field()
        p_e = scrapy.Field()
        p_s = scrapy.Field()
        f_p_e = scrapy.Field()
        peg = scrapy.Field()
        p_c = scrapy.Field()
        quick_ratio = scrapy.Field()
        current_ratio = scrapy.Field()
        debt_eq = scrapy.Field()
        sma20 = scrapy.Field()
        sma50 = scrapy.Field()
        sma200 = scrapy.Field()
        volume = scrapy.Field()
        avg_volume = scrapy.Field()
        rsi = scrapy.Field()
        roa = scrapy.Field()
        roe = scrapy.Field()
        roi = scrapy.Field()
        gross_margin = scrapy.Field()
        oper_margin = scrapy.Field()
        profit_margin = scrapy.Field()
        shs_outstand = scrapy.Field()
        shs_float = scrapy.Field()
        short_float = scrapy.Field()
        short_ratio = scrapy.Field()
        target_price = scrapy.Field()
        high_y = scrapy.Field()
        low_y = scrapy.Field()
        price = scrapy.Field()
        change = scrapy.Field()
        prev_close = scrapy.Field()
        eps = scrapy.Field()
        sales_q_to_q = scrapy.Field()
        eps_q_to_q = scrapy.Field()
        insider_own = scrapy.Field()
        insider_trans = scrapy.Field()
        inst_own = scrapy.Field()
        inst_trans = scrapy.Field()
        dividend = scrapy.Field()
        dividend_percent = scrapy.Field()
        employees = scrapy.Field()
        recom = scrapy.Field()
