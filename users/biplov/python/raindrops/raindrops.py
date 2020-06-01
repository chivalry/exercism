def convert(number):
    if (number % 3 != 0) and (number % 5 != 0) and (number % 7 != 0):
    	return str(number)

    else:
    	a=[0,0,0]
    	b = {0:'Pling', 1:'Plang', 2:'Plong'}
    	return_text = ''

    	if (number % 3 == 0):
    		a[0]=1
    	if (number %5 ==0):
    		a[1]=1
    	if (number %7 ==0):
    		a[2]=1

    	for i in range(0,3):
    		if a[i] == 1:
    			return_text += b[i]

    	return return_text









