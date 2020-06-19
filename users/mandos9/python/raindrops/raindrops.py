def convert(number):
    sounds = [(3,"Pling"), (5, "Plang"), (7, "Plong")]

    sound =  "".join(sound[1] for sound in sounds if number % sound[0] == 0)
    return sound if sound is not "" else str(number)
