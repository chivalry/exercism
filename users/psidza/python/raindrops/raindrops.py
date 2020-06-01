def convert(number):
    result=''
    hasfactor=False
    if number%3==0:
        result+='Pling'
        hasfactor=True
    if number%5==0:
        result+='Plang'
        hasfactor=True
    if number%7==0:
        result+='Plong'
        hasfactor=True
    if hasfactor==False:return str(number)
    return result