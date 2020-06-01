def convert(number):
    s = ''
    s += 'Pling' if number % 3 == 0 else s 
    s += 'Plang' if number % 5 == 0 else s
    s += 'Plong' if number % 7 == 0 else s
    return s if s else str(number)
