def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("You must provide strands of equal length")

    differences = [t for t in zip(strand_a, strand_b) if t[0] != t[1]]
    return len(list(differences))
