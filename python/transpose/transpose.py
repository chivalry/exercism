def transpose(text):
    result = []
    for line_idx, line in enumerate(text.splitlines()):
        for char_idx, char in enumerate(line):
            while len(result) <= char_idx:
                result.append([])
            while len(result[char_idx]) < line_idx:
                result[char_idx].append(' ')
            result[char_idx].append(char)
    return '\n'.join(''.join(row) for row in result)
