def is_paired(input_string):
    if not input_string:
        return True
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in input_string:
        if c in pairs.values():
            stack.append(c)
        if c in pairs.keys():
            try:
                if pairs[c] != stack.pop():
                    return False
            except:
                return False
    return not bool(stack)
