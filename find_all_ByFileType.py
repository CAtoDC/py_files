'''Find all filetypes using glob'''

import os, glob

os.chdir("/home/mark/Pictures/backgrounds")

for file in glob.glob("*.jpg"):
    print(file)
