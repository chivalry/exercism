def convert(number):
    returnstring=""
    if number%3 == 0:
        returnstring+="Pling"
    if number%5 == 0:
        returnstring+="Plang"
    if number%7 == 0:
        returnstring+="Plong"
    if not ((number%3==0) or (number%5==0) or (number%7==0)):
        returnstring=str(number)
    return returnstring

print(convert(5))
