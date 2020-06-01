def convert(i: int) -> str:
    result = ''
    if i % 3 == 0:
        result += 'Pling'
    if i % 5 == 0:
        result += 'Plang'
    if i % 7 == 0:
        result += 'Plong'
    if result == '':
        result = str(i)
    return result