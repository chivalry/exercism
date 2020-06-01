def to_rna(dna_strand):
    m = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    rna = ''
    for c in dna_strand:
        rna += m[c]
    return rna
