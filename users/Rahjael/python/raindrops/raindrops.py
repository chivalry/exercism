def convert(number):

    has_3 = True if (number % 3) == 0 else False
    has_5 = True if (number % 5) == 0 else False
    has_7 = True if (number % 7) == 0 else False

    if not (has_3 or has_5 or has_7):
        return str(number)
    else:
        answer = ''
        
        if has_3:
            answer += 'Pling'
        if has_5:
            answer += 'Plang'
        if has_7:
            answer += 'Plong'

        return answer
        
    
