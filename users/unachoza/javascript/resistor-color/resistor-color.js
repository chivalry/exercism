//
// This is only a SKELETON file for the 'Resistor Color' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
//   const COLORS = {
//   'Black': 0,
//   'Brown': 1,
//   'Red': 2,
//   'Orange': 3,
//   'Yellow': 4,
//   'Green': 5,
//   'Blue': 6,
//   'Violet': 7,
//   'Grey': 8,
//   'White': 9,
// };
export const colorCode = (color) => {
  let lookup = color.replace(color.charAt(0), color.charAt(0).toUpperCase());
  return COLORS[lookup];
};

export const COLORS = {
  Black: 0,
  Brown: 1,
  Red: 2,
  Orange: 3,
  Yellow: 4,
  Green: 5,
  Blue: 6,
  Violet: 7,
  Grey: 8,
  White: 9,
};
colorCode('Black');
