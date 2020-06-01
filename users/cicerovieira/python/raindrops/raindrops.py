def convert(number):
    if number % 105 == 0:
        print("PlingPlangPlong")
    elif number % 15 == 0:
        print("PlingPlang")
    elif number % 21 == 0:
        print("PlingPlong")
    elif number % 35 == 0:
        print("PlangPlong")
    elif number % 3 == 0:
        print("Pling")
    elif number % 5 == 0:
        print("Plang")
    elif number % 7 == 0:
        print("Plong")
    else:
        print(number)


# 28 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
convert(28)
# 30 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang".
convert(30)
# 34 is not factored by 3, 5, or 7, so the result would be "34".
convert(34)

convert(1)
convert(3)
convert(5)
convert(7)
convert(6)
convert(8)
convert(9)
convert(10)
convert(14)
convert(15)
convert(21)
convert(25)
convert(27)
convert(35)
convert(49)
convert(52)
convert(105)
convert(3125)
