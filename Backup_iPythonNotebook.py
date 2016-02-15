# This backs up files and directories in the
# from the path in "source"

import os
import time

source = ['"C:\\Users\Mark\Documents\IPython Notebooks"']

target_dir = 'C:\Users\Mark\Dropbox\Backup'

# Create target directory if it is not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

# The current day is the name of the subdirectory 
# in the main directory
today = target_dir + os.sep + time.strftime('%Y%m%d')

# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = raw_input('Enter a comment --> ')

# Check if comment was entered
if len(comment) == 0:
	target = today + os.sep + '.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace(' ', '_') + '.zip'

# Create subdirectory if not already there
if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory', today

# Use the zip command to put files in zip archive
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

# Run the backup
print "Zip command is:"
print zip_command
print "Running:"
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup failed'
