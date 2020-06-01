def convert(number=0):
    num = int(number)
    result = ""
    #making mod
    res1 = num % 3
    res2 = num % 5
    res3 =  num % 7
      

    if res1 == 0: result += "Pling"
    if res2 == 0: result += "Plang"
    if res3 == 0: result += "Plong"
    if result == "": return print(str(num))

convert()