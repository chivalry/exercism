def convert(number):
    result = ""

    #the number doesn't have 3, 5 or 7 as a factor
    if number%3!=0 and number%5!=0 and number%7!=0:
        result = str(number)

    #the number has 3 as a factor 
    if number%3==0:
        result += "Pling"
        
    #the number has 5 as a factor
    if number%5==0:
        result += "Plang"
        
    #the number has 7
    if number%7==0:
        result += "Plong"
    
    return result

