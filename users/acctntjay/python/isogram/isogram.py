def is_isogram(string):
    stringlst = [v for v in sorted(string.casefold()) if v.isalpha()]
    for i,v in enumerate(stringlst) :
        if stringlst[i] == stringlst[i-1] :
            return False
    return True
