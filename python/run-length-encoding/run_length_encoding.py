def decode(string):
    result = ''
    count = ''
    for char in string:
        if char.isnumeric():
            count += char
        else:
            result += char * int(count if len(count) else 1)
            count = ''
    return result


def encode(string):
    if not string:
        return ''
    letter = ''
    count = 0
    result = ''
    for char in string:
        if letter != char:
            result += '' if letter == '' else count_ge_1(count) + letter
            letter = char
            count = 1
        else:
            count += 1
    result += count_ge_1(count) + letter
    return result


def count_ge_1(count):
    return str('' if count == 1 else count)


print(decode('2AB3CD4E'))
