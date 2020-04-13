from string import ascii_uppercase, whitespace, ascii_uppercase


def response(hey_bob: str):
    is_all_caps = hey_bob == hey_bob.upper() and any([c for c in hey_bob if c in ascii_uppercase])
    if not hey_bob or hey_bob.split() == []:
        return 'Fine. Be that way!'
    if hey_bob[-1] == '?' and is_all_caps:
        return "Calm down, I know what I'm doing!"
    if hey_bob.strip()[-1] == '?':
        return 'Sure.'
    if is_all_caps:
        return 'Whoa, chill out!'
    return 'Whatever.'

    
if __name__ == '__main__':
    print(response('WHAT\'S GOING ON?'))
