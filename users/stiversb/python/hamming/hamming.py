"""
    module hamming.py
    Implements hamming distance per exercism exercise spec at:
    https://exercism.io/my/solutions/1f92764daa734e08bcc4faf4dde31e96
"""


def distance(strand_a, strand_b):
    """ function distance - inputs are two lists of bases
        output is the hamming distance between those bases.
        ValueError raised for incorrect formatting/length of lines of bases.
    """
    if not len(strand_a) == len(strand_b):
        raise ValueError("Invalid inputs: Strands unequal/invalid")
    return sum([1 for a_base, b_base in zip(strand_a, strand_b) if a_base != b_base])
