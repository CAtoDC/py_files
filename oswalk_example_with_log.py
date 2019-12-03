import os

'''
This script recursively walks the current directory and the directories within it. 

This version writes the result to a log file (findfiletype.log). The log file is opened in append mode; it will not overwrite a log file that exists already, it will only append to the file. 

https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/
'''

# The top argument for walk
topdir = '.'

# The extension to search for
exten = '.txt'
logname = 'findfiletype.log'

# What will be logged
results = str()
 
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            # Save to results string instead of printing
            results += '%s\n' % os.path.join(dirpath, name)
 
# Write results to logfile
with open(logname, 'w') as logfile:
    logfile.write(results)

