def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must have the same length")
    return len([c for i, c in enumerate(strand_a) if strand_a[i] != strand_b[i]])
