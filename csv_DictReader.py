import csv

'''
This was taken from Cory Shafer's "Python Tutorial: Real World Example - Parsing Names From a CSV to an HTML List" (https://www.youtube.com/watch?v=bkpLhQd6YQM)

Patrons.csv is an anonymized list of patrons who contributed to his site.
The first few lines are informative, not actual names, so we ignore those.
Everything after: "No Reward,Description: (None for No Reward),,,,,," are patrons who do not want to be listed.

We can also use csv.reader, but csv.DictReader allows us to use the field names.
The result is formatted for the web (standard HTML).
'''

html_output = ''
names = []

with open('data/patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # We don't want the first bad line of data
    next(csv_data)

    for cell in csv_data:
        if cell['FirstName'] == 'No Reward':
            break
        names.append(f"{cell['FirstName']} {cell['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)