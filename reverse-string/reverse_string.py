def reverse(text):
    s = ''
    for i in range(1, len(text)+1):
        s += text[-i]
    return s
