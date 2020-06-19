def distance(dna_1, dna_2):
    if len(dna_1) != len(dna_2):
        raise ValueError('Strands not of same length')
    return sum(1 for _1, _2 in zip(dna_1, dna_2) if _1 != _2)
