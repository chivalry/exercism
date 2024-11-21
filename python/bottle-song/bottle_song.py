NUMBERS = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'
}


def recite(start, take=1):
    if take == 0:
        return []
    word = NUMBERS[start]
    result = [
        f'{word.capitalize()} green {plural_bottle(start)} hanging on the wall,',
    ] * 2
    left = 'no' if start == 1 else NUMBERS[start - 1]
    plural = plural_bottle(start - 1)
    result.extend([
        'And if one green bottle should accidentally fall,',
        f"There'll be {left} green {plural} hanging on the wall."
    ])
    result.append('')
    result.extend(recite(start=start - 1, take=take - 1))
    return result if take > 1 else result[:-1]


def plural_bottle(count):
    return f'bottle{"" if count == 1 else "s"}'
