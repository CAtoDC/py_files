'''Quick way to view header and record count'''

import csv

filename = "data/chicago_rats.csv"

with open(filename, newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header, '\n')
    
    for row in reader:
        count = reader.line_num
        
    print ('Total records:', "{:,}".format(count))
    