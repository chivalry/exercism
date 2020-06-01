def convert(number):
    str_list = []
    if number % 3 == 0:
        str_list.append('Pling')
    if number % 5 == 0:
        str_list.append('Plang')
    if number % 7 == 0:
        str_list.append('Plong')

    return ''.join(str_list) if str_list else str(number)
