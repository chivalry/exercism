def convert(number):
    raindrop=''
    # prime factor cases - any or all, in this order:
    if 0==number%3:
        raindrop+='Pling'
    if 0==number%5:
        raindrop+='Plang'
    if 0==number%7:
        raindrop+='Plong'
    #very hackerish drop-thru clause:
    if ''==raindrop:
        raindrop=str(number)
    return raindrop

