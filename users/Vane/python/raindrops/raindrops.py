def convert(number):
    result=''
    A = number % 3 #factor of 3
    B = number % 5 #factor of 5
    C = number % 7 #factor of 7
    if A==0:     #is a factor of 3
        result += 'Pling'
    if B==0:     #is a factor of 5
        result += 'Plang'
    if C==0:     #is a factor of 7
        result += 'Plong'
    if A!=0 and B!=0 and C!=0: #not a factor of 3,5, and 7
        result = number
    return result

print(convert(34))
        
    
