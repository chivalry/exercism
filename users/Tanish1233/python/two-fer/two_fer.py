def two_fer(name):
    if name==None:
        return "One for you, one for me"
    elif not name.isalpha():
         return "Only input names."
    else:
        return "One for " + name + " , one for me"









