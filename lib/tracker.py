#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : carrack.py                                         ##
# Description : Main program                                       ##
#####################################################################

# Standard Packages
import json

# External Packages
import click
import requests
import yfinance as yf

# Project Packages:
import lib.auth as auth

def arg_preprocessing(ticker_list):
    ticker_str = ""
    for ticker in ticker_list:
        ticker_str += ticker.upper() + ","

    ticker_str = ticker_str[:-1]
    return ticker_str

def get_data(ticker_str):
    #self._base_url = 'https://query1.finance.yahoo.com'
    #self._scrape_url = 'https://finance.yahoo.com/quote'
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
        price_dict[ticker] = stock_data['regularMarketPrice']

    return price_dict

def track_market(ticker_list):
    source = 'alphavantage'
    ticker_str = arg_preprocessing(ticker_list)
    print(ticker_str)
    stock_data_dict = get_data(ticker_str)
    #print(stock_data)
    price_dict = get_price(stock_data_dict)
    #print(price_dict)
    return price_dict



"""
    #apikey = auth.get_api_key(source)
    #url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFTAAPL&interval=5min&apikey={}".format(apikey)
    #       https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
    #url = "https://api.polygon.io/v1/last/stocks/TWTR?&apiKey={}".format(apikey)
"""
