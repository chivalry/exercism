def convert(number):
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return "{}".format(number)
    else:
        raindrops = ""
        if(number % 3 == 0):
            raindrops += "Pling"
        if(number % 5 == 0):
            raindrops += "Plang"
        if(number % 7 == 0):
            raindrops += "Plong"
        return raindrops
    pass
