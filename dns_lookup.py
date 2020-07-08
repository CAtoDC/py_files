'''DNS Lookup using socket'''

import socket

addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')

print ("Google DNS: " + addr1)
print ("Yahoo DNS: " + addr2)
