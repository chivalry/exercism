
def convert(number):
    three_factor = number % 3
    five_factor = number % 5
    seven_factor = number % 7
    result_1 = ""
    result_2 = ""
    result_3 = ""
    if three_factor == 0:
        result_1 = 'Pling'
    if five_factor == 0:
        result_2 = 'Plang'
    if seven_factor == 0:
        result_3 = 'Plong'

    result = result_1 + result_2 + result_3

    if not result:
        return (str(number))
    else:
        return(result)
    
  


