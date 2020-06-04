export const toRna = (inputDNA) => {
  let outputRNA = [];

  inputDNA.split('').forEach((letter) => {
    switch (letter) {
      case 'G':
        outputRNA.push('C');
        break;
      case 'C':
        outputRNA.push('G');
        break;
      case 'T':
        outputRNA.push('A');
        break;
      case 'A':
        outputRNA.push('U');
        break;
      default:
        outputRNA.push('');
        break;
    }
  });
  return outputRNA.join('');
};
