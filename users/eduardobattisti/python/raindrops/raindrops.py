#!usr/bin/python3

def convert(number):
    raindrop = str()
    factors_numbers = {3 : "Pling", 5 : "Plang", 7 : "Plong"}


    for factor in factors_numbers:
        if number % factor == 0:
            raindrop += factors_numbers[factor]
    
    return raindrop if raindrop else str(number)
