//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const hey = (message) => {
    const msg = message.trim();
    if (msg.length == 0) {
        return 'Fine. Be that way!';
    }
    const is_yelling = (msg.toUpperCase() == msg) && (/[A-Z]/g).test(msg);
    const is_question = msg.slice(-1) == '?';
    if (is_yelling && is_question) {
        return "Calm down, I know what I'm doing!";
    }
    if (is_yelling) {
        return 'Whoa, chill out!';
    }
    if (is_question) {
        return 'Sure.';
    }
    return 'Whatever.';
};
