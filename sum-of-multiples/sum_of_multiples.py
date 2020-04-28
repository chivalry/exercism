def sum_of_multiples(limit, multiples):
    return sum({i for j in multiples for i in range(1, limit) if j and i % j == 0})
