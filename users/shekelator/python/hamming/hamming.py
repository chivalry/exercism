def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(f"Strands not the same length: '{strand_a}'' vs. '{strand_b}'")

    differences = len([x for ind,x in enumerate(strand_a) if strand_a[ind] != strand_b[ind]])
    return differences
