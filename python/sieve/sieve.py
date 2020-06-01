def primes(limit):
    if limit <= 2:
        return [] if limit < 2 else [2]
    buf = {}
    for num in range(2, limit+1):
        if num not in buf:
            buf[num] = True
            for candidate in range(num * 2, limit+1, num):
                buf[candidate] = False
    return sorted([x for x in buf if buf[x]])

if __name__ == '__main__':
    print(primes(10))
