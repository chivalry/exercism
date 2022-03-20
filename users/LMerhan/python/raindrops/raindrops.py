def convert(number):
    a = number % 3 == 0  # 'Pling'
    b = number % 5 == 0  # 'Plang'
    c = number % 7 == 0  # 'Plong'

    if a and b and c:
        return 'PlingPlangPlong'
    elif a and b:
        return 'PlingPlang'
    elif a and c:
        return 'PlingPlong'
    elif b and c:
        return 'PlangPlong'
    elif c:
        return 'Plong'
    elif b:
        return 'Plang'
    elif a:
        return 'Pling'
    else:
        return str(number)