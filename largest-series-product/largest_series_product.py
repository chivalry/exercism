def largest_product(series, size):
    if (not series and size) or size < 0 or size > len(series):
        raise ValueError('invalid parameters')
    if not size:
        return 1
    mx = 0
    series = [int(c) for c in series]
    for i in range(len(series)-size+1):
        prod = 1
        for j in range(i, i+size):
            prod *= int(series[j])
        if prod > mx:
            mx = prod
    return mx
