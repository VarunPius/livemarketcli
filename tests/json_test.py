import requests

def get_data(ticker_str):
    url = 'https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols={}'.format(ticker_str)

    getData = requests.get(url)
    requests_data = getData.json() # json.loads(getData.text)

    print(requests_data['quoteResponse']['result'])

    return

#get_data("AAPL,MSFT")
get_data("CRIS")
