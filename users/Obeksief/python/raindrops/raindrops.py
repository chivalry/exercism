def convert(number):
    mot = ""
    if number%3==0:
    	mot=mot+"Pling"
    if number%5==0:
    	mot=mot+"Plang"
    if number%7==0:
    	mot=mot+"Plong"
    if number%3!=0 and number%5!=0 and number%7!=0:
    	mot="{}".format(number)
    return (mot)

