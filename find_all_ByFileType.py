'''Find all filetypes using glob'''

import os, glob

os.chdir("C:/Users/Mark/Pictures")

for file in glob.glob("*.jpg"):
    print(file)
