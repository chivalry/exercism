def convert(number):
    
    conversions={3:'Pling',5:'Plang',7:'Plong'}

    result=''.join(i[1] for i in conversions.items() if number % i[0] == 0)

    if result=='': return str(number)
    else: return result

