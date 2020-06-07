export const gigasecond = (date) => {
  let calculatedDate = new Date(date);
  calculatedDate.setUTCSeconds(calculatedDate.getUTCSeconds() + 1000000000);
  return calculatedDate;
};
