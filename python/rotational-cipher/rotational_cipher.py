def rotate(text, key):
    result = ''
    for char in text:
        if not char.isalpha():
            result += char
            continue
        diff = 97 if ord(char) >= 97 else 65
        result += chr((ord(char) - diff + key) % 26 + diff)
    return result
