def convert(number):
    string = ""
    hit = 0
    if (number % 3 == 0):
        string = string + 'Pling'
        hit = 1
    if (number % 5 == 0):
        string = string + 'Plang'
        hit = 1
    if (number % 7 == 0):
        string = string + 'Plong'
        hit = 1
    
    if (hit ==  0):
        return str(number)

    return string
    
