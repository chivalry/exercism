GIFTS = [
    "twelve Drummers Drumming,",
    "eleven Pipers Piping,",
    "ten Lords-a-Leaping,",
    "nine Ladies Dancing,",
    "eight Maids-a-Milking,",
    "seven Swans-a-Swimming,",
    "six Geese-a-Laying,",
    "five Gold Rings,",
    "four Calling Birds,",
    "three French Hens,",
    "two Turtle Doves, and",
    "a Partridge in a Pear Tree.",
]

ORDINALS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


def recite(start_verse: int, end_verse: int) -> [str]:
    """Returns the list of verses of the song "Twelve days of Christmas"
    starting at start_verse, and ending at end_verse"""
    return [
        f"On the {ORDINALS[i]} day of Christmas my true love gave to me: "
        f"{' '.join(GIFTS[-(i+1):])}"
        for i in range(start_verse - 1, end_verse)
    ]
