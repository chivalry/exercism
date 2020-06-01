def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError('strand_a and strand_b need to be of equal lengths')
  
    return sum(nucleotide[0] != nucleotide[1] for nucleotide in zip(strand_a, strand_b))