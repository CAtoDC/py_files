# example of continue and break
# from Automate the Boring Stuff with Python
# you can use continue and break statements only inside while and for loops. 
# If you try to use these statements elsewhere, Python will give you an error.


while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
