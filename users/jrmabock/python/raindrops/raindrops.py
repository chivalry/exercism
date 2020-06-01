
def convert(number):
    empty_string = ""
    if number %3 == 0:
        empty_string += "Pling"
    if number %5 == 0:
        empty_string += "Plang"
    if number %7 == 0:
        empty_string += "Plong"
    if not number %3 == 0 and not number %5 == 0 and not number %7 == 0 :
        empty_string = str(number)
    return empty_string




