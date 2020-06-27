import xml.etree.ElementTree as ET
import xmltodict
import json

''' This program converts an xml file to json 
    XML can be tricky to convert; this may need some more testing
    Source: https://towardsdatascience.com/the-easy-way-to-work-with-csv-json-and-xml-in-python-5056f9325ca9
    
    Online XML to JSON converter:  http://www.utilities-online.info/xmltojson/#.XuDTRs9Kjw8
    
'''

tree = ET.parse('data/books.xml')
xml_data = tree.getroot()

xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')


data_dict = dict(xmltodict.parse(xmlstr))

print(data_dict)

with open('data/new_data_2.json', 'w+') as json_file:
    json.dump(data_dict, json_file, indent=4, sort_keys=True)
    