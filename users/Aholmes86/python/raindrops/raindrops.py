def convert(number):
	value_returned = ""
	if number % 3 == 0:
		value_returned += "Pling"
	if number % 5 == 0:
		value_returned += "Plang"
	if number % 7 == 0:
		value_returned += "Plong"
	if value_returned == "":
		value_returned = str(number)
	return value_returned
