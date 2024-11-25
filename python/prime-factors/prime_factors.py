from typing import List
from time import time


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


def factors(value: int) -> List:
    if value in [2, 3]:
        return [value]
    facts = []
    limit = int(value ** 0.5) + 1
    while value > 1:
        for candidate in range(2, limit):
            if candidate == 306290:
                candidate
            if is_prime(candidate) and value % candidate == 0:
                facts.append(candidate)
                value //= candidate
                if is_prime(value):
                    facts.append(value)
                    value //= value
        if value == 1:
            break
    return sorted(facts)


t0 = time()
print(factors(93819012551))
t1 = time()
print(t1 - t0)
