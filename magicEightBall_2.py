import random
messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'Outlook not so good',
    'Very doubtful',
    'My reply is no'
]
print(messages[random.randint(0, len(messages) - 1)])