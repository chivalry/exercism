def convert(number):
    drop = input()
    if drop % 3 == 1:
        print("Pling")
    elif drop % 5 == 1:
        print("Plang")
    elif drop % 7 == 1:
        print("Plong")
    else:
        print(drop)
    pass
