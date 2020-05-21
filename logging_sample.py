import logging

'''
Although this does not produce an error, the value is wrong because the 
variables are strings.

Logging Levels
YouTube:  Albert Sweigart, "Logging and Testing and Debugging, Oh My!", PyBay2017
https://docs.python.org/3.7/howto/logging.html

- DEBUG
- INFO
- WARN
- ERROR
- CRITICAL
'''

logging.basicConfig(filename='logging_sample.txt', level=logging.DEBUG)  # filename is optional
#logging.disable(logging.CRITICAL)

print('Enter the first number: ')
first = input()
logging.debug(type(first))
print('Enter the second number: ')
second = input()
logging.debug(type(second))
print('The sum of', first, 'and', second, 'is', first+second)

