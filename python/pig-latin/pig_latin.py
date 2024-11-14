def translate(text):
    result = []
    for word in text.split():
        result.append(translate_word(word))
    return ' '.join(result)
    
def translate_word(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if word.startswith(vowels + ('xr', 'yt')):
        return word + 'ay'
    if word.startswith('qu'):
        return word[2:] + 'quay'
    consonants = ''
    result = None
    for i, char in enumerate(word):
        if char not in vowels:
            consonants += char
            if word[i+1] in vowels + ('y',):
                result = word[i+1:] + consonants + 'ay'
                break
            if word[i+1] + word[i+2] == 'qu':
                result = word[i+3:] + word[:i+3] + 'ay'
                break
    return result