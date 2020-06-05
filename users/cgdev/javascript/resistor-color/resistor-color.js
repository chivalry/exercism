//
// This is only a SKELETON file for the 'Resistor Color' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

 export const colorCode = (color) => {
    let mappedColors = COLORS.map((_, index) => index);
    return mappedColors[COLORS.findIndex((el) => el === color.toLowerCase())];
};

 export const COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"];