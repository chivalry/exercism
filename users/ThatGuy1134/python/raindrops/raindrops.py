def convert(number):
    rain = ""
    aMap = {3 : "Pling", 5 : "Plang", 7 : "Plong"}
    
    for key in aMap:
        if (number % key) == 0:
            rain += aMap[key]

    if len(rain) > 0:
        return rain
    else:
        return str(number)
