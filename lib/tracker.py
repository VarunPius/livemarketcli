import click
import requests
import json

def auth():
    with open('data/auth.json') as f:     # Location is wrt project; not current file
        data = json.load(f)
        apikey = data['alphavantage']['apikey']
        print(apikey)
