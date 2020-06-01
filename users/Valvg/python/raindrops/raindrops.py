def convert(number):
    lst = []

    if (number % 3 == 0):
        lst.append("Pling")

    if (number % 5 == 0):
        lst.append("Plang")

    if (number % 7 == 0):
        lst.append("Plong")

    if (len(lst) == 0):
        return str(number)
    else:
        return ''.join(lst)
