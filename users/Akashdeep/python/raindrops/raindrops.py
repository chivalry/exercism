def convert(number):
    stre=""
    if(number%3==0 or number%5==0 or number%7==0):
        if number%3==0:
            stre+="Pling"
        if number%5==0:
            stre+="Plang"
        if number%7==0:
            stre+="Plong"
        return stre
    else:
        return str(number)
