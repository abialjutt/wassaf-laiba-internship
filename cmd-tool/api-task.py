import json
import requests


API_URL = 'http://api.icndb.com/jokes/random'


def get_response(url=API_URL):
    res = requests.get(url)
    return res


x = get_response()
print(x.json)
joke = x.json()['value']['joke']
print(joke)
