def convert(number):
    result = ""
    is_factor = False 
    if number % 3 == 0: 
        result = "Pling"
        is_factor = True
    if number % 5 == 0: 
        result += "Plang"
        is_factor = True
    if number % 7 == 0: 
        result += "Plong"
        is_factor = True
    return result if is_factor else str(number)
        
