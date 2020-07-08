'''Read through a file with csv

csv reader converts each row to a list of strings as they're read.

The header row is printed out first - and then the total count.

If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correctly.
It should always be safe to specify newline='', since the csv module does its own (universal) newline handling.
'''

import csv, sys

filename = 'data/titanic3.csv'

count = 0
with open(filename, newline='') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(headers, '\n')    
    try:
        for row in reader:
            count = reader.line_num
            #print (row)

        print ('Total records:', "{:,}".format(count))
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))