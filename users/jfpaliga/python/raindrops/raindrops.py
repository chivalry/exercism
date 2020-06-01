def convert(number):
    string = ''
    if number % 3 == 0:
        string = string + 'Pling'
    if number % 5 == 0:
        string = string + 'Plang'
    if number % 7 == 0:
        string = string + 'Plong'
    
    if string == '':
        print(number)
    else:
        print(string)
