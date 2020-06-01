def is_pangram(sentence):
    sentence = sentence.lower()
    for c in range(ord('a'), ord('z')+1):
        if chr(c) not in sentence:
            return False
    return True
