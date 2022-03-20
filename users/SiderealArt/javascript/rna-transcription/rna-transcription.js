var dict = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
};
export const toRna = (dna_strand) => {
    let strand = dna_strand.split('');
    strand = strand.map(a => dict[a]);
    return strand.join('');
};