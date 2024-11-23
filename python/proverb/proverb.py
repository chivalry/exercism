def proverb(*args, qualifier=None):
    if not args:
        return []
    conclusion = f'And all for the want of a {qualifier + " " if qualifier else ""}{args[0]}.'
    if len(args) == 1:
        return [conclusion]
    result = ([f'For want of a {word} the {args[idx + 1]} was lost.'
               for idx, word in enumerate(args[:-1])])
    result.append(conclusion)
    return result
