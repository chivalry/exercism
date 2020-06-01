from math import inf


def largest(max_factor: int, min_factor: int = 0):
    if min_factor > max_factor:
        raise ValueError('none in range')
    buf = [0, None]
    for prod, fact in palindromes(mn=min_factor, mx=max_factor):
        if prod == buf[0]:
            buf[1].append(fact)
        elif prod > buf[0]:
            buf[0] = prod
            buf[1] = [fact]
    if buf[0] == 0:
        return None, []
    return buf[0], tuple(buf[1])


def smallest(max_factor: int, min_factor: int = 0):
    if min_factor > max_factor:
        raise ValueError('none in range')
    buf = [inf, None]
    for prod, fact in palindromes(mn=min_factor, mx=max_factor):
        if prod == buf[0]:
            buf[1].append(fact)
        elif prod < buf[0]:
            buf[0] = prod
            buf[1] = [fact]
    if buf[0] == inf:
        return None, []
    return buf[0], tuple(buf[1])


def palindromes(mx: int, mn: int = 0):
    return set([(i * j, (i, j)) for i in range(mn, mx+1) for j in range(i, mx+1) if is_palindrome(str(i * j))])


def is_palindrome(word: str):
    if len(word) in [0, 1]:
        return True
    return word[0] == word[-1] and is_palindrome(word[1:-1])


if __name__ == '__main__':
    print(largest(mn=1, mx=9))
