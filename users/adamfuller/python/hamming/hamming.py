def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
       raise ValueError('No hamming distance for strands of different lengths')

    return len([1 for n, dna in enumerate(strand_a) if dna != strand_b[n]])
