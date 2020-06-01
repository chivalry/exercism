import re


def count_words(sentence):
    sentence = sentence.lower().replace('_', ' ')
    sentence = re.sub(r"(\w)'(\w)", r'\1_\2', sentence)
    words = re.findall(r'\w+', sentence)
    counts = {}
    for word in words:
        word = word.replace('_', "'")
        counts[word] = counts.get(word, 0) + 1
    return counts

if __name__ == '__main__':
    print(count_words('here are some words'))