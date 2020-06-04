

export const toRna = (input) => {
  let rnaOf = { 
    G : 'C',
    C : 'G',
    T : 'A',
    A : 'U'
  };
  return [].map.call(input, (c) => rnaOf[c]).join("");
};
