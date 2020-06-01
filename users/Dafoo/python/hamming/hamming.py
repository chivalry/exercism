def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Not equal length")
    else:
        counter = 0
        for a, b in zip(strand_a, strand_b):
            if a == b:
                pass
            else:
                counter += 1
        return counter
