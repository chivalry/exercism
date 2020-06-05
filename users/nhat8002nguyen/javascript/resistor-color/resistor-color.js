//
// This is only a SKELETON file for the 'Resistor Color' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const colors = new Map();
    colors.set("black", 0);
    colors.set("brown", 1);
    colors.set("red", 2);
    colors.set("orange", 3);
    colors.set("yellow", 4);
    colors.set("green", 5);
    colors.set("blue", 6);
    colors.set("violet", 7);
    colors.set("grey", 8);
    colors.set("white", 9);


export const colorCode = (color) => {
//   throw new Error("Remove this statement and implement this function");
    return colors.get(color);
};

export const COLORS = Object.keys(colors);
