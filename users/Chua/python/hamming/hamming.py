def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        ham_dist = 0
        for _ in range(len(strand_a)):
            if strand_a[_] != strand_b[_]:
                ham_dist += 1
        return ham_dist
    else:
        raise ValueError("Strands needs to be of equal length")