def convert(number):
    raindrop_sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    output = [raindrop_sounds[k] for k in raindrop_sounds if not bool(number % k)]

    if len(output):
        return "".join(output)
    return str(number)

