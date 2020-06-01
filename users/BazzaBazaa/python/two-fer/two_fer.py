def two_fer(name = None):
    if name is None:
        return "One for you, one for me."
    else:
        return "One for " + name +", one for me."
print(two_fer("alice"))
print(two_fer("bob"))
print(two_fer())
