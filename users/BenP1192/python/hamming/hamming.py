def is_different(a, b):
    return 0 if a == b else 1

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands of different lengths")
    
    difference = [is_different(strand_a[index],strand_b[index]) for index in range(len(strand_a))]
    return sum(difference)
