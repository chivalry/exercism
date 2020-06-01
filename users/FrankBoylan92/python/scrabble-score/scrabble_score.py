def score(word):
    scores = {1:["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]}
    key_list = list(scores.keys()) 
    val_list = list(scores.values())

    return sum(sum(key for key in scores if letter in scores[key] for letter in word.upper()))
    return sum(sum(key_list[i] for i in range(len(val_list)) if letter in val_list[i]) for letter in word.upper())
