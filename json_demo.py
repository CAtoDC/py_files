''' JavaScript Object Notation
JSON            Python
object          dict
array           list
string          str
number(int)     int
number(real)    float
true            True
false           False
null            None
'''


import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john-smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true            
        }
    ]
}
'''

# load json string into python object
data = json.loads(people_string)

# Demonstrate datatype conversions
print(type(data))   # dict
print(type(data['people']))   # list

# show only names
for person in data['people']:
    print(person['name'])

# remove phone number
for person in data['people']:
    del person['phone']

# now dump it back into a string
# we can also sort keys with sort_keys=True
new_string = json.dumps(data, indent=2)
print(new_string)

