import xml.etree.ElementTree as ET
'''
Source: https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2
'''

tree = ET.parse('data/CFR-2020-title12-vol1.xml')
root = tree.getroot()

print(root.tag)  # CFRDOC

for child in root:
  print(child.tag, child.attrib)


for doc in root.iter('CFRDOC'):
  print(doc.attrib)


# Loop through text of SUBJECT field (case-sensitive)
for subject in root.iter('SUBJECT'):
    print(subject.text)



# START HERE
# find text through loop
# for movie in root.findall("./genre/decade/movie/[year='1992']"):
#     print(movie.attrib)

# for item in root.findall("./CFRDOC/TITLE/CFRTITLE/TITLEHD/[HD='Title 12']"):
#   print(item.attrib)

