def convert(number):
    if number % 3 == 0:
        return "Pling"
    elif number % 5 == 0:
        return "Plang"
    elif number % 7 == 7:
        return "Plong"
    else:
        return number
