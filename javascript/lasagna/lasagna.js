// @ts-check

/**
 * The number of minutes it takes to prepare a single layer.
 */
const MINUTES_PER_LAYER = 2;
const EXPECTED_MINUTES_IN_OVEN = 40;

/**
 * Determines the number of minutes the lasagna still needs to remain in the
 * oven to be properly prepared.
 *
 * @param {number} minutes
 * @returns {number} the number of minutes remaining
 */
export function remainingMinutesInOven(minutes) {
  return EXPECTED_MINUTES_IN_OVEN - minutes;
}

/**
 * Given a number of layers, determines the total preparation time.
 *
 * @param {number} layers
 * @returns {number} the total preparation time
 */
export function preparationTimeInMinutes(layers) {
  return MINUTES_PER_LAYER * layers;
}

/**
 * Calculates the total working time. That is, the time to prepare all the layers
 * of lasagna, and the time already spent in the oven.
 *
 * @param {number} layers
 * @param {number} minutes
 * @returns {number} the total working time
 */
export function totalTimeInMinutes(layers, minutes) {
  return minutes + preparationTimeInMinutes(layers);
}

export { EXPECTED_MINUTES_IN_OVEN };
