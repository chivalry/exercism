def flatten(iterable):
    result = []
    for elem in iterable:
        if hasattr(elem, '__iter__'):
            result.extend(flatten(elem))
        elif elem is not None:
            result.append(elem)
    return result
