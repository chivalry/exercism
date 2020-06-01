def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('DNA strands must be the same size')
    diff = 0
    for index, nucleotide in enumerate(strand_a):
        if strand_a[index] != strand_b[index]:
            diff += 1
    return diff
