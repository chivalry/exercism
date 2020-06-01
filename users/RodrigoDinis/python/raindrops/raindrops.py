def convert(number):
    to_return = ""
    if number % 3 == 0:
        to_return += "Pling"
    if number % 5 == 0:
        to_return += "Plang"
    if number % 7 == 0:
        to_return += "Plong"
    if to_return == "":
        to_return = str(number)
    return to_return
