'''JavaScript Object Notation
The load method loads a file into a python object.
The loads method loads a string into a python object.
The dump method converts the data to a JSON file.
The dumps method converts the data to a JSON string.
'''

import json

# load method load a file into a python object
with open('data/states.json') as f:
  data = json.load(f)

for state in data['states']:
  print(state['name'], state['abbreviation'])

# delete the area codes
for state in data['states']:
  del state['area_codes']

# now convert the new data to a JSON file
with open('data/new_states.json', 'w') as f:
  json.dump(data, f, indent=2)

