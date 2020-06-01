def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(
            f'Strands must at equal length strand_a is:{len(strand_a)} and strand_b is:{len(strand_b)}')
    defects = 0
    for pair in zip(strand_a, strand_b):
        if pair[0] != pair[1]:
            defects += 1
    return defects
