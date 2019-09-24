import os

'''
os.walk takes 4 arguments and only the first is mandatory. 
The arguments (and their default values) in order are:

top - the root of the directory to walk.
topdown(=True) - boolean designating top-down or bottom-up walking.
onerror(=None) - name of a function to call if an error occurs.
followlinks(=False) - boolean designating whether or not to follow symbolic links.  

The only one we are concerned with here is the first. The Python 3.x version produces a generator function. This means that the Python 3.x version will only go to the next iteration when we tell it to, and the way we will do that is with a loop.
'''
 
# The top argument for walk
topdir = '.'
 
# The extension to search for
exten = '.txt'
 
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            print(os.path.join(dirpath, name))

