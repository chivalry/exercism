def convert(number):
	three = ""
	five = ""
	seven = ""
	if (number % 3) != 0 and (number % 5) != 0 and (number % 7) != 0:
		#print(str(number))
		return(str(number))
		
	else:
		if (number % 3) == 0:
			three = "Pling"
		if (number % 5) == 0:
			five = "Plang"
		if (number % 7) == 0:
			seven = "Plong"
		#print(three+five+seven)
		return(three+five+seven)
	pass

"""
def test():
	n = 8
	convert(n)

test()
"""
