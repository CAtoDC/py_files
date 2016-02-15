word = 'banana'
count = 0

# look into each element of the string
for letter in word:
    if letter == 'b':
        print ('We have a b!')
        count = count + 1
    elif letter != 'b':
        print("No 'b' here.")

# let's keep things grammatically correct
if count == 1:
    print (("There is only ") + str(count) + (" b in ") + word + ("."))
elif count > 1:
    print (("There are only ") + str(count) + (" b's in ") + word + ("."))
