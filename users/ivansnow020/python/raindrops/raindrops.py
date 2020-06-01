def convert(number):
    if type(number) != int:
        raise Exception("Input must be an integer")
    output = ""
    mark = 0
    if number % 3 == 0:
        mark = 1
        output += "Pling"
    if number % 5 == 0:
        mark = 1
        output += "Plang"
    if number % 7 == 0:
        mark = 1
        output += "Plong"
    if mark == 0:
        output = str(number)
    return output
