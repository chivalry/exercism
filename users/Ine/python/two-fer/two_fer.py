#I just wanted to reach out to whomever is taking a look at this and thank them.
#I'm pretty nervous stepping into this space but I'm very excited and I want to acknowledge the work that you're doing to make that possible for me.
#So.. Thank you! :)

def two_fer(name='you'):
    '''
    Asks for a string and returns "One for {name}, one for me"
    Unless the name returned is empty. Then the program inserts "you."
    '''
    return("One for " + name + ", one for me.")
    #Here I knew I wanted to take care of this in a single line without if statements,
    #but I wasn't sure how to incorporate capitalize() without using list comprehension or
    #having it catch the default 'you'.
def two_fer2(name='you'):
    '''
    Asks for a string and returns "One for {name}, one for me"
    Unless the name returned is empty. Then the program inserts "you."
    '''
    if name == 'you':
        return("One for you, one for me.")
    else:
        return("One for " + name.capitalize() + ", one for me.")
