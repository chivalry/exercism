def convert(number):
    test = ''
    if not bool(number % 3):
        test += "Pling"
    if not bool(number % 5):
        test += "Plang"
    if not bool(number % 7):
        test += "Plong"
    if (test == ""):
        test = str(number)
    return test
