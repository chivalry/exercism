const rnaMap = { G: 'C', C: 'G', T: 'A', A: 'U' };

export const toRna = (inputDNA) => {
  return inputDNA.split('').map(x => rnaMap[x]).join('');
};
