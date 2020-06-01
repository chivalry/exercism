def say(num):
    if num < 0 or num >= 1e12:
        raise ValueError('only pass positive integers')
    if num == 1:
        return 'zero'

def say_up_to_99(number):
    pass