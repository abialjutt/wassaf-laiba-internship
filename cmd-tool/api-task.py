import json
import requests
res = requests.get('http://api.icndb.com/jokes/random')
print(res.json)
joke = res.json()['value']['joke']
print(joke)
