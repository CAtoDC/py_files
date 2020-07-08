import os, glob
'''Find all filetypes using glob'''

os.chdir("/home/mark/Pictures/backgrounds")

for file in glob.glob("*.jpg"):
    print(file)
