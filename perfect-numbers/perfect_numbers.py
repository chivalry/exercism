def classify(num):
    if num <= 0:
        raise ValueError('can only classify natural numbers')
    sum = aliquot_sum(num)
    if num == sum:
        return 'perfect'
    if num > sum:
        return 'deficient'
    return 'abundant'


def factors(num):
    facs = []
    for i in range(1, num+1):
        if num % i == 0:
            facs.append(i)
    return facs


def aliquot_sum(num):
    return sum(factors(num)[:-1])
