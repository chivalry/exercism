export const toRna = (strand) => {
    const dict = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    return strand.split('').map(x => dict[x]).join('')
};
