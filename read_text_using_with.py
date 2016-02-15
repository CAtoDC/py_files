"""
Opening and closing text files using with

Use only for reasonably sized text files
"""


# Pythonic
# close happens automatically when using "with"
with open('sample_text/LoremIpsum.txt') as f:
	data = f.read()
	
print (data)
