def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError("The strands are different lengths")

    return sum([1 for item in zip(strand_a, strand_b) if item[0] != item[1]])
