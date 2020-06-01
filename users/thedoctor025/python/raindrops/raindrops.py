def convert(number):
    result = ''
    divisible = False
    if number % 3 == 0:
        result += 'Pling'
        divisible = True
    if number % 5 == 0:
        result += 'Plang'
        divisible = True
    if number % 7 == 0:
        result += 'Plong'
        divisible = True
    if not divisible:
        result = str(number)
    return result
