from re import fullmatch
def distance(string1, string2):
    hamming = 0
    string1 = string1.upper()
    string2 = string2.upper()
    if len(string1) == len(string2):
        if fullmatch(r'[ACGT]*', string1) and fullmatch(r'[ACGT]*', string2):
            for letter1, letter2 in zip(string1, string2):
                if not letter1 == letter2:
                    hamming += 1
            return 'distance between the strings {0} and {1} is {2} '.format(string1, string2, hamming)
        else:
            return "one of those string is not well typing "
    else:
        raise TypeError ("the strings entered don't have the same length ")

c = distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
print(c)