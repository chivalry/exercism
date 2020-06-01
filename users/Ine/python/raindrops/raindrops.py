def convert(num):
    '''
    Enter a a string that contains raindrop sounds corresponding to certain potential factors.
    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
    '''
    answer = ''
    if num % 3 == 0:
        answer = answer + 'Pling'
    if num % 5 == 0:
        answer = answer + 'Plang'
    if num % 7 == 0:
        answer = answer + 'Plong'
    if answer != '':
        return answer
    else:
        return str(num)