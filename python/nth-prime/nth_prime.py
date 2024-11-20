def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    temp = None
    gen = primes()
    for _ in range(number):
        temp = next(gen)
    return temp


def primes():
    i = 1
    while True:
        i += 1
        if is_prime(i):
            yield i


def is_prime(num: int) -> bool:
    """Uses early prime facts to determine primacy more quickly."""
    if not isinstance(num, int) or num <= 0:
        raise ValueError('Error: Only positive integers can be prime')
    if num in [2, 3, 5, 7]:
        return True
    if num < 2 or num % 2 == 0 or num == 9:
        return False
    if num % 3 == 0:
        return False
    root = int(num ** 0.5)
    fact = 5
    while fact <= root:
        if num % fact == 0 or num % (fact + 2) == 0:
            return False
        fact += 6
    return True
