"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique_count value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def sum_of(dice, number):
    return len([x for x in dice if x == number]) * number

def score(dice, category):
    dice_set = set(dice)
    unique_vals = list(dice_set)
    unique_count = len(unique_vals)

    if category == YACHT:
        return 50 if unique_count == 1 else 0
    if category == CHOICE:
        return sum(dice)
    if category == BIG_STRAIGHT:
        return 30 if dice_set == set([2, 3, 4, 5, 6]) else 0
    if category == LITTLE_STRAIGHT:
        return 30 if dice_set == set([1, 2, 3, 4, 5]) else 0
    if category == FOUR_OF_A_KIND:
        if unique_count == 1:
            return sum(dice) - dice[0]
        if unique_count != 2:
            return 0
        die_1 = unique_vals[0]
        die_2 = unique_vals[1]
        if dice.count(die_1) == 4:
            return die_1 * 4
        if dice.count(die_2) == 4:
            return die_2 * 4
        return 0
    if category == FULL_HOUSE:
        if unique_count != 2:
            return 0
        die_1 = unique_vals[0]
        die_2 = unique_vals[1]
        if (dice.count(die_1) == 2 or dice.count(die_2) == 2):
            return sum(dice)
        return 0
    return sum_of(dice, category - 1)
