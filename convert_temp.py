# Best Practice - use Try/Except block when getting user input

inp = input('Enter temperature in Fahrenheit: ')

try:
    fahr = float(inp)

    # Convert to Celsius
    cel = (fahr - 32.0) * 5.0 / 9.0
    cel = int(cel)

    print ("In Celsius, that's " + str(cel) + " degrees.")
except:
    print ('Please enter a number')