import json 
import csv 

'''
This program converts json files to csv files.
'''

# path of json file to convert
data_to_convert = 'data/employees.json'
#data_to_convert = 'data/states.json'

# path of csv file to create
csv_file = 'data/emp_data_file.csv'
#csv_file = 'data/states_data_file.csv'

# name of json object
json_object = 'emp_details'
#json_object = 'states'


# Opening JSON file and load data
with open(data_to_convert) as json_file: 
	data = json.load(json_file) 

object_data = data[json_object] 
#employee_data = data['states']

# open a file for writing 
data_file = open(csv_file, 'w') 

# create the csv writer object 
csv_writer = csv.writer(data_file) 

# Set counter for writing headers to the csv file 
count = 0

for obj in object_data: 
	if count == 0: 

		# Write headers of CSV file
		header = obj.keys() 
		csv_writer.writerow(header) 
		count += 1

	# Writing data of CSV file 
	csv_writer.writerow(obj.values()) 

data_file.close() 
