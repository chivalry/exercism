def abbreviate(words):
    words = words.replace("-", " ")
    words = words.replace("_", " ")

    return ''.join(item[0] for item in words.split()).upper()
