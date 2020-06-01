def convert(number):
    result = ""

    raindrops = [
        (3, "Pling"),
        (5, "Plang"),
        (7, "Plong"),
    ]

    for factor, drop in raindrops:
        if number % factor == 0:
            result += drop

    if not result:
        result = str(number)

    return result
