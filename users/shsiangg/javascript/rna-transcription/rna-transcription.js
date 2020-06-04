//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const toRna = (dna) => {
  const dna_to_rna_mapping = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
  }
  let rna = ''
  for (const nuc of dna) {
    rna += dna_to_rna_mapping[nuc]
  }
  return rna
};
