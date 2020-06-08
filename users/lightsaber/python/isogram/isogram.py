def is_isogram(string):
    freq_count = [0]*26

    for char in string:
        if char.islower():
            freq_count[ord(char) - ord('a')] += 1
        elif char.isupper():
            freq_count[ord(char) - ord('A')] += 1

    for freq in freq_count:
        if freq > 1:
            return False

    return True