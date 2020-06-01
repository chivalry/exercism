#!/usr/bin/env python3


from string import ascii_letters


def is_isogram(string):
    result = [i for i in string.lower() if string.lower().count(i) > 1 and i in ascii_letters]
    return True if not result else False
