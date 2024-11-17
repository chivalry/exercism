def transform(legacy_data):
    result = {}
    for key in legacy_data:
        for char in legacy_data[key]:
            result[char.lower()] = key
    return result
