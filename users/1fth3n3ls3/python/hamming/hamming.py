def distance(strand_a, strand_b):
    if len(strand_b) != len(strand_a):
        raise ValueError("Chains length don't match!")
    
    pairs = zip(strand_a, strand_b)

    return sum(1 for each in pairs if each[1] != each[0])
