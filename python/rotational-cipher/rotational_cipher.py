def rotate(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    map = alpha[key:] + alpha[:key]
    translation = str.maketrans((alpha + alpha.upper()),
                                (map + map.upper()))
    return text.translate(translation)
