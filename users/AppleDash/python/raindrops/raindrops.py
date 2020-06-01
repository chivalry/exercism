# returns True if f is a factor of n.
def is_factor(n, f):
    return n % f == 0

def convert(number):
    raindrops = ""

    if is_factor(number, 3):
        raindrops += "Pling"

    if is_factor(number, 5):
        raindrops += "Plang"

    if is_factor(number, 7):
        raindrops += "Plong"

    if not raindrops:
        raindrops = str(number)

    return raindrops

