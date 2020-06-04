
export const toRna = (stringToTest) => {

  let input = stringToTest.split("");
  let rna = "";

  let nucleotides = {
    'C': 'G',
    'G': 'C',
    'T': 'A',
    'A': 'U',
  }

  for (let i = 0; i < input.length; i++) {
    rna += nucleotides[input[i]];
  }

  return rna;
};
