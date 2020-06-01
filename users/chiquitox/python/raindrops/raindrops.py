def convert(number):
    sound = ""
    
    if(not number%3): sound = sound + "Pling"
    if(not number%5): sound = sound + "Plang"
    if(not number%7): sound = sound + "Plong"
    
    if(len(sound)>0): return sound
    else: return sound + str(number)
