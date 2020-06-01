# - has 3 as a factor, add 'Pling' to the result.
# - has 5 as a factor, add 'Plang' to the result.
# - has 7 as a factor, add 'Plong' to the result.

def convert(number):
    result = ""
    if number % 3 is 0:
        result += "Pling"
    if number % 5 is 0:
        result += "Plang"
    if number % 7 is 0:
        result += "Plong"
    if result is "":
        return str(number)
    else:
        return result
