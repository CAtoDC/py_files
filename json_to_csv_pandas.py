'''
Converts json to csv using pandas

Source:  https://datatofish.com/json-string-to-csv-python/
'''

import pandas as pd

df = pd.read_json (r'data.json')

df.to_csv (r'cfr_data.csv', index = None)