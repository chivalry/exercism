def two_fer(name="you"):
    '''if name == "" or None:
        name = "you"
    else:
        pass'''
    #response = "One for {}, one for me.".format(name)
    response = f"One for {name}, one for me"
    print(response)
    return response

two_fer()