def two_fer(name = None):
    if name == None or type(name) != str:
        return 'One for you, one for me.'
    else:
        return f'One for {name}, one for me.'

print(two_fer())