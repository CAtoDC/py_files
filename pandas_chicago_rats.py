'''Pandas example from David Beasley'''

import pandas

# read a csv file, skipping the last line
rats = pandas.read_csv('c:/py/data/chicago_rats.csv')

#print rats   #180,051 rows

# investigate range of values for a certain field
print (rats['Current Activity'].unique())

# filter the data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
print (len(crew_dispatched), 'crews were dispatched.')

# group by completion date
dates = crew_dispatched.groupby('Completion Date')
print (len(dates), 'incidents were completed. \n')

# determine the counts on each day
date_counts = dates.size()
print (date_counts[0:10], '\n')


# sort the counts
date_counts.sort_values(inplace=True)
print (date_counts[-10:], '\n')

# find the 10 most rat-infested zip codes in chicago
# This doesn't work. Not sure why.
print('Zip Code', ' ', 'Incident Calls')
print (crew_dispatched['ZIP Code'].value_counts())
