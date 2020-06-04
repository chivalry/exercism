var dict = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
};
export const toRna = (dna_strand) => {
    var a = '';
    for (var i = 0; i < dna_strand.length; i++) {
        a += dict[dna_strand[i]];
    }
    return a;
};