def convert(number):
    val = ""
    if number % 3 == 0:
        val = "Pling"
    if number % 5 == 0:
        val = val + "Plang"
    if number % 7 == 0:
        val = val + "Plong"

    if len(val) == 0:
        val = str(number)
    return val
