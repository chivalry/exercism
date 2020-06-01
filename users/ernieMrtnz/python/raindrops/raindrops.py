# - has 3 as a factor, add 'Pling' to the result.
# - has 5 as a factor, add 'Plang' to the result.
# - has 7 as a factor, add 'Plong' to the result.


def convert(number):
    sound = ''
    if number % 3 == 0:
        sound += 'Pling'
    if number % 5 == 0:
        sound += 'Plang'
    if number % 7 == 0:
        sound += 'Plong'
    if sound == '':
        return str(number)
    else:
        return sound
