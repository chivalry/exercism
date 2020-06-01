def convert(number):
    raindrop = ""
    if number % 3 == 0:
        raindrop = "Pling"
    if number % 5 == 0:
        raindrop += "Plang"
    if number % 7 == 0:
        raindrop += "Plong"
    if len(raindrop) > 0:
        return raindrop
    return str(number)

