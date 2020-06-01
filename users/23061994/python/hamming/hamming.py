def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA lengths are not the same")
    pairs = zip(list(strand_a), list(strand_b))
    mistake = sum([k != v for k, v in pairs])
    return mistake
