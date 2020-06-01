from typing import Dict, List


days: Dict[int, Dict[str, str]] = {
    1: {'ord': 'first', 'verse': 'and a Partridge in a Pear Tree.'},
    2: {'ord': 'second', 'verse': 'two Turtle Doves'},
    3: {'ord': 'third', 'verse': 'three French Hens'},
    4: {'ord': 'fourth', 'verse': 'four Calling Birds'},
    5: {'ord': 'fifth', 'verse': 'five Gold Rings'},
    6: {'ord': 'sixth', 'verse': 'six Geese-a-Laying'},
    7: {'ord': 'seventh', 'verse': 'seven Swans-a-Swimming'},
    8: {'ord': 'eighth', 'verse': 'eight Maids-a-Milking'},
    9: {'ord': 'ninth', 'verse': 'nine Ladies Dancing'},
    10: {'ord': 'tenth', 'verse': 'ten Lords-a-Leaping'},
    11: {'ord': 'eleventh', 'verse': 'eleven Pipers Piping'},
    12: {'ord': 'twelfth', 'verse': 'twelve Drummers Drumming'}
}


def recite(start_verse: int, end_verse: int):
    if start_verse > 12:
        return []
    buf: str = f'On the {days[start_verse]["ord"]} day of Christmas my true love gave to me: '
    buf += ''.join([f'{days[i]["verse"]}, ' for i in range(start_verse, 1, -1)])
    buf += days[1]['verse'] if start_verse > 1 else days[1]['verse'].replace('and ', '')
    buf: List[str] = [buf]
    if start_verse == end_verse:
        return buf
    buf.extend(recite(start_verse + 1, end_verse))
    return buf
