'''With dictreader, we access the elements of each row using the row headers. 
For example, row['name'] or row['age']

Very efficient
'''

import csv

filename = "data/titanic3.csv"

with open(filename) as f:
    reader = csv.DictReader(f)
    
    header = next(reader)
    print(header, '\n')
    
    for row in reader:
        count = reader.line_num
        print (row['name'], '-' , row['age'])
        
    print ('Total records:', "{:,}".format(count))