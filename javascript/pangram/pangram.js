export const isPangram = (sentence) => {
    const candidate = sentence.toLowerCase();
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
    return alphabet.every((c) => candidate.includes(c));
};
