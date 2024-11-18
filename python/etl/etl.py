def transform(legacy_data):
    result = {}
    for key in legacy_data:
        for char in legacy_data[key]:
            result[char.lower()] = key
    return result


'''mentor comprehension code
def transform(legacy_data):
    return {char: score for score, chars in legacy_data.items() for char in map(str.lower, chars)}
'''
