//
// This is only a SKELETON file for the 'Resistor Color' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const colorCode = (param) => {
  let colorArr = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
  let value = 0;
  colorArr.forEach((e, index) => {
      if (e === param) {
        value = index;
      }
  });
  return value;
};

export const COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"];

