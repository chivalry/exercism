def convert(number):
	x= int(number)
	if x%3==0 and x%5==0 and x%7==0:
		return ("PlingPlangPlong")
	if x%5==0 and x%7==0:
		return ("PlangPlong")
	if x%3==0 and x%7==0:
		return ("PlingPlong")
	if x%3==0 and x%5==0:
		return ("PlingPlang")
	if x%3 ==0:
		return ("Pling")
	if x%5==0:
		return ("Plang")
	if x%7==0:
		return ("Plong")	
	else:
		return(str(x))
