def convert(number):
    returned_sound = ""

    if number % 3 == 0:
        returned_sound += "Pling"
    if number % 5 == 0:
        returned_sound += "Plang"
    if number % 7 == 0:
        returned_sound += "Plong"

    return returned_sound or str(number)
