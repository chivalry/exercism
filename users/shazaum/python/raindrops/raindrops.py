def convert(n):
    s = ""
    s += "Pling" if n % 3 == 0 else ""
    s += "Plang" if n % 5 == 0 else ""
    s += "Plong" if n % 7 == 0 else ""
    s += str(n) if not s else ""
    return s
