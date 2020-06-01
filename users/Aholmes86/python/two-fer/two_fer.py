def two_fer(*name):
	if name:
		formatted_string = 'One for {}, one for me.'.format(name[0])
		return formatted_string
	return "One for you, one for me."	
