//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const toRna = (seq) => {
  const baseMap = {
    G: 'C',
    C : 'G',
    T : 'A',
    A : 'U'
  }
  if (seq.length === 0) {
    return ''
  }
  let rna = ''
  for(var i = 0; i <= seq.length - 1; i++) {
    rna += baseMap[seq[i]]
  }
  return rna
};
