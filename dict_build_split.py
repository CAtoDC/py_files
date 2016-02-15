"""
Building and Splitting Dictionaries
    
Combine two lists to form a dict using zip
"""

# zip combines the two lists and dict puts them
# in a key/value pair

given_name = ['John', 'Eric', 'Terry', 'Michael']
family_name = ['Cleese', 'Idle', 'Gilliam', 'Palin']

pythons = dict(zip(given_name, family_name))
print(pythons)
