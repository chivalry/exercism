def two_fer(name):
    print("One for " + name + " , one for me")

name= input("Type your name: ")
if len(name)==0:
    print("One for you, one for me")
elif not name.isalpha():
    print("Only input names.")
else:
    two_fer(name)
