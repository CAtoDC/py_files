import string
''' When working between platforms, it is often necessary to convert 
the line endings on files for them to work, especially when it comes to code. 
Pass Unix Python code with \r and it goes nowhere. Same on Mac Python with \n. 
This code simply and easily fixes the problem.
'''
def convert_line_endings(temp, mode):
    #modes:  0 - Unix, 1 - Mac, 2 - DOS
    if mode == 0:
        temp = string.replace(temp, '\r\n', '\n')
        temp = string.replace(temp, '\r', '\n')
    elif mode == 1:
        temp = string.replace(temp, '\r\n', '\r')
        temp = string.replace(temp, '\n', '\r')
    elif mode == 2:
        import re
        temp = re.sub("\r(?!\n)|(?<!\r)\n", "\r\n", temp)
    return temp
