"""
Isolate the domain by finding @ and a space (i.e. @gmail.com )
in a line of text.
"""

#Find domain in messy email text
data = 'From mark.cuevas@gmail.com Sat Jan 5 09:14:16:2008'
at_position = data.find('@')
print (at_position)

space_position = data.find(' ', at_position)
print (space_position)

host = data[at_position + 1 : space_position]
print (host)
