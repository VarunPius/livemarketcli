import json

def get_api_key(source):
    apikey = ""
    if source == 'alphavantage':
        apikey = get_alphavantage_api()
    elif source == 'polygon':
        apikey = get_polygon_api()
    return apikey


def get_alphavantage_api():
    with open('data/auth.json') as f:     # Location is wrt project; not current file
        data = json.load(f)
        apikey = data['alphavantage']['apikey']
        return apikey

def get_polygon_api():
    with open('data/auth.json') as f:     # Location is wrt project; not current file
        data = json.load(f)
        apikey = data['polygon']['apikey']
        return apikey
