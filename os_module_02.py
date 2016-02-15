'''Rename files programmatically'''
import os

os.chdir('/Users/Mark/Music/Shorty Rogers and His Giants')
print (os.getcwd(), '\n')

for f in os.listdir():
    print(f)
    
