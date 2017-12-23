''' Read json file 


Pretty print keeps things aligned
'''

import json
from pprint import pprint

# Reading data back
with open('data/widgets.json', 'r') as f:
     data = json.load(f)

# pretty print keeps things aligned
pprint(data)
