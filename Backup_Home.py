# This backs up files and directories in the
# from the path in "source"


import os
import time

source = ['"C:\\Users\Mark\Documents\_Home"']

target_dir = 'C:\Users\Mark\Dropbox\Backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

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
