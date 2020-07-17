'''List files programmatically'''
import os

os.chdir('/home/mark/Music/')
print (os.getcwd(), '\n')

for f in os.listdir():
    print(f)
    
