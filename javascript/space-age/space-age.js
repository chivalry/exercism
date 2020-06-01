export const age = (planet, seconds) => {
    let dict = {
        'earth': 1,
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447496,
        'uranus': 84.016846,
        'neptune': 164.79132
    };
    return parseFloat((seconds / 31557600 / dict[planet]).toFixed(2))
};
