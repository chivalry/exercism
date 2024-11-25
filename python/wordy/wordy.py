OPERATORS = ['plus', 'minus', 'multiplied_by', 'divided_by']


def answer(question):
    if not question.startswith('What is') or not question.endswith('?'):
        raise ValueError('unknown operation')
    question = question.removeprefix('What is ').removesuffix('?').replace(' by', '_by')
    if question.endswith('cubed'):
        raise ValueError('unknown operation')
    if len(question) == 0:
        raise ValueError('syntax error')
    tokens = question.split(' ')
    if len(tokens) % 2 != 1:
        raise ValueError('syntax error')
    if len(tokens) == 1 and isInt(tokens[0]):
        return int(tokens[0])
    digit_tokens = [token for token in tokens[::2]]
    print(digit_tokens)
    if any([not isInt(digit_token) for digit_token in digit_tokens]):
        raise ValueError('syntax error')
    op_tokens = [token for token in tokens[1::2]]
    if any([op_token not in OPERATORS for op_token in op_tokens]):
        raise ValueError('unknown operation')
    result = int(digit_tokens[0])
    for idx, token in enumerate(op_tokens):
        digit = int(digit_tokens[idx + 1])
        match token:
            case 'plus':
                result += digit
            case 'minus':
                result -= digit
            case 'multiplied_by':
                result *= digit
            case 'divided_by':
                result /= digit
    return result


def isInt(token):
    contains_sign = token[0] in ['-', '+']
    return (contains_sign and token[1:].isdigit()) or token.isdigit()
