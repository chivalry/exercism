//
// This is only a SKELETON file for the 'Resistor Color' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
export let COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"];

export const colorCode = (x) => {
  if(x == COLORS){
    return COLORS;
  } else {
    for(let i = 0; i < COLORS.length; i++){
      if(x == COLORS[i]){
        return COLORS.indexOf(x);
      }
    }
  }
};