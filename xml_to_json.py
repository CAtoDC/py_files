# Program to convert an xml file to json file 
# We can then convert to csv with this: https://csvjson.com/json2csv
  
# import json module and xmltodict 
# both modules provided by python 
import json 
import xmltodict 
  
  
# open the input xml file and read data in form of python dictionary using xmltodict module 
# Added encoding and now it works
with open("data/CFR-2020-title12-vol1.xml", encoding="utf8") as xml_file: 
      
    data_dict = xmltodict.parse(xml_file.read()) 
    xml_file.close() 
      
    # generate the object using json.dumps()  
    # corresponding to json data 
      
    json_data = json.dumps(data_dict) 
      
    # Write the json data to output  
    # json file 
    with open("data.json", "w") as json_file: 
        json_file.write(json_data) 
        json_file.close()