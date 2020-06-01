def convert(number):
    aux1 = number % 3
    aux2 = number % 5
    aux3 = number % 7
    if aux1 == aux2 == aux3 == 0:
        return "PlingPlangPlong"
    if aux1 == aux2 == 0 and aux3 !=0:
        return "PlingPlang"
    if aux1 == aux3 ==0 and aux2 !=0:
        return "PlingPlong"
    if aux1 != 0 and aux2 == aux3 ==0:
        return "PlangPlong"
    if aux1 == 0 and aux2 != 0 and aux3 != 0:
        return "Pling"
    if aux1 != 0 and aux2 == 0 and aux3 != 0:
        return "Plang"
    if aux1 != 0 and aux2 != 0 and aux3 == 0:
        return "Plong"
    else:
        return str(number)
 
