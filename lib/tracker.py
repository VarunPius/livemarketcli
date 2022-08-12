#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : tracker.py                                         ##
# Description : Implementation to fetch values and process data    ##
#####################################################################

# Standard Packages
import json

# External Packages
import click
import requests

# Project Packages:
import lib.auth as auth


################################################################################
# Program starts here
################################################################################

def arg_preprocessing(ticker_list):
    ticker_str = ""
    # alternatively, you can do this: 
    # ticker_str = ",".join(ticker_list)
    for ticker in ticker_list:
        ticker_str += ticker.upper() + ","

    ticker_str = ticker_str[:-1]
    return ticker_str

def get_data(ticker_str):
    url = 'https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols={}'.format(ticker_str)

    getData = requests.get(url)
    requests_data = getData.json() # json.loads(getData.text)

    ticker_dict = {}

    for i in range(len(requests_data['quoteResponse']['result'])):
        symbol = requests_data['quoteResponse']['result'][i]['symbol']
        ticker_dict[symbol] = requests_data['quoteResponse']['result'][i]

    return ticker_dict

def get_price(stock_data_dict):
    price_dict = {}
    for ticker, stock_data in stock_data_dict.items():
        price_dict[ticker] = {}
        price_dict[ticker]['current_price'] = 0.0
        price_dict[ticker]['marketState'] = stock_data['marketState']
        if price_dict[ticker]['marketState'] == 'PRE':
            price_dict[ticker]['current_price'] = stock_data.get('preMarketPrice') if not None else stock_data['regularMarketPrice']
            price_dict[ticker]['current_change'] = stock_data.get('preMarketChange') if not None else stock_data['regularMarketChange']
            price_dict[ticker]['current_change_percent'] = stock_data.get('preMarketChangePercent') if not None else stock_data['regularMarketChangePercent']
        elif price_dict[ticker]['marketState'] == 'REGULAR':
            price_dict[ticker]['current_price'] = stock_data['regularMarketPrice']
            price_dict[ticker]['current_change'] = stock_data['regularMarketChange']
            price_dict[ticker]['current_change_percent'] = stock_data['regularMarketChangePercent']
        elif price_dict[ticker]['marketState'] == 'POST':
            price_dict[ticker]['current_price'] = stock_data['postMarketPrice']
            price_dict[ticker]['current_change'] = stock_data['postMarketChange']
            price_dict[ticker]['current_change_percent'] = stock_data['postMarketChangePercent']
        elif price_dict[ticker]['marketState'] == 'POSTPOST' or price_dict[ticker]['marketState'] == 'PREPRE':
            price_dict[ticker]['current_price'] = stock_data['postMarketPrice']
            price_dict[ticker]['current_change'] = round(stock_data['postMarketPrice'] - stock_data['regularMarketPreviousClose'], 3)
            price_dict[ticker]['current_change_percent'] = round((stock_data['postMarketPrice'] - stock_data['regularMarketPreviousClose'])/stock_data['regularMarketPreviousClose'], 5)*100

        price_dict[ticker]['regularMarketPreviousClose'] = stock_data['regularMarketPreviousClose']
        price_dict[ticker]['regularMarketOpen'] = stock_data['regularMarketOpen']
        price_dict[ticker]['regularMarketPrice'] = stock_data['regularMarketPrice']
        price_dict[ticker]['regularMarketTime'] = stock_data['regularMarketTime']
        price_dict[ticker]['regularMarketChange'] = stock_data['regularMarketChange']
        price_dict[ticker]['regularMarketChangePercent'] = stock_data['regularMarketChangePercent']
        price_dict[ticker]['regularMarketDayHigh'] = stock_data['regularMarketDayHigh']
        price_dict[ticker]['regularMarketDayLow'] = stock_data['regularMarketDayLow']

        if price_dict[ticker]['marketState'] == 'POST' or price_dict[ticker]['marketState']== 'POSTPOST':
            price_dict[ticker]['postMarketPrice'] = stock_data['postMarketPrice']
            price_dict[ticker]['postMarketChange'] = stock_data['postMarketChange']
            price_dict[ticker]['postMarketChangePercent'] = stock_data['postMarketChangePercent']

    return price_dict

def track_market(ticker_list):
    source = 'alphavantage'
    ticker_str = arg_preprocessing(ticker_list)
    #print(ticker_str)
    stock_data_dict = get_data(ticker_str)
    price_dict = get_price(stock_data_dict)
    return price_dict


################################################################################
# Rough
################################################################################

"""
    #apikey = auth.get_api_key(source)
    #url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFTAAPL&interval=5min&apikey={}".format(apikey)
    #       https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
    #url = "https://api.polygon.io/v1/last/stocks/TWTR?&apiKey={}".format(apikey)
"""
