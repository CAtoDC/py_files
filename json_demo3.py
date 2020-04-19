'''
Retrieve a json file from the web
'''

import json
from urllib.request import urlopen

# this site no longer works
# most free sites these days require a (free) api key
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
  source = response.read()

data = json.loads(source)

#print(json.dumps(data, indent=2))

usd_rates = dict()  # empty dict

for item in data['list']['resources']:
  name = item['resource']['fields']['name']
  price = item['resource']['fields']['price']
  #print(name, price)
  usd_rates[name] = price  # key/value pairs for dict

print(usd_rates['USD/EUR'])

# 50 US dollars in Euros
print(50 * float(usd_rates['USD/EUR']))
