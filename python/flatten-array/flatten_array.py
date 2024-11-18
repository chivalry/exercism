from collections.abc import Iterable


def flatten(iterable):
    result = []
    for elem in iterable:
        '''original code:
        if hasattr(elem, '__iter__'):
        '''
        if isinstance(elem, Iterable):
            result.extend(flatten(elem))
        elif elem is not None:
            result.append(elem)
    return result
