def convert(number):
    result = ""
    for divider in range(3, 9, 2):
        if number % divider == 0:
            if divider == 3:
                result = result + "Pling"
            if divider == 5:
                result = result + "Plang"
            if divider == 7:
                result = result + "Plong"
    if result == "":
        return str(number)
    else:
        return result


