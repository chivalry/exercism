def convert(number):
    rain_drop = ''
    if number % 3 == 0:
        rain_drop += 'Pling'
    if number % 5 == 0:
        rain_drop += 'Plang'
    if number % 7 == 0:
        rain_drop += 'Plong'
    return rain_drop if rain_drop else str(number)
