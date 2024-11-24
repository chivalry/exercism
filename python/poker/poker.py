STRAIGHT_FLUSH = 10
FOUR_OF_A_KIND = 9
FULL_HOUSE = 8
FLUSH = 7
STRAIGHT = 6
THREE_OF_A_KIND = 5
TWO_PAIR = 4
ONE_PAIR = 3
HIGH_CARD = 2
NO_HIGH_HAND = 1

HAND_RANKS = [
    STRAIGHT_FLUSH, FOUR_OF_A_KIND, FULL_HOUSE, FLUSH, STRAIGHT,
    THREE_OF_A_KIND, TWO_PAIR, ONE_PAIR, HIGH_CARD
]

CARD_RANKS = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']


def best_hands(hands: list[str]) -> list[str]:
    '''Return a the hand or list of hands that have the highest rank
    :param hands: list[str] - The hands to compare
    :return list[str] - The one or more hands that have the highest rank
    '''
    if len(hands) == 1:
        return [hands[0]]
    highest_rank = NO_HIGH_HAND
    high_hands = []
    structured_hands = build_hand_map(hands)
    for structured_hand in structured_hands:
        hand = structured_hands[structured_hand]
        if is_straight_flush(hand):
            highest_rank = STRAIGHT_FLUSH
            high_hands += [hand]
        elif highest_rank < FOUR_OF_A_KIND and is_four_of_a_kind(hand):
            highest_rank = FOUR_OF_A_KIND
            high_hands += [hand]
        elif highest_rank < FULL_HOUSE and is_full_house(hand):
            highest_rank = FULL_HOUSE
            high_hands += [hand]
        elif highest_rank < FLUSH and is_flush(hand):
            highest_rank = FOUR_OF_A_KIND
            high_hands += [hand]
        elif highest_rank < STRAIGHT and is_straight(hand):
            highest_rank = FOUR_OF_A_KIND
            high_hands += [hand]
        elif highest_rank < THREE_OF_A_KIND and is_three_of_a_kind(hand):
            highest_rank = FOUR_OF_A_KIND
            high_hands += [hand]
        elif highest_rank < TWO_PAIR and is_two_pair(hand):
            highest_rank = FOUR_OF_A_KIND
            high_hands += [hand]
        elif highest_rank < ONE_PAIR and is_one_pair(hand):
            highest_rank = FOUR_OF_A_KIND
            high_hands += [hand]
    return [' '.join(high_hand) for high_hand in high_hands]


def build_hand_map(hands: list[str]) -> dict[str, list[str]]:
    """Build a structure where the text hand is the key and the sorted hand is the value
    :param hands: list[str] - The hands to build the structure from
    :return dict[str, list[str]] - The structure to return
    """
    return {hand: sort(hand) for hand in hands}


def sort(hand: str) -> list[str]:
    """Return a sorted version of the hand as a list of cardds
    :param hand: str - The hand to sort as a string of cards
    :return list[str] - The sorted hand, high card to low, as a list of card strings
    """
    return sorted(hand.split(' '), key=card_rank)


def card_rank(card: str) -> int:
    """Return the rank of the given card
    :param card: str - A string representing the card
    :return int - The rank of the card, lower being better
    """
    return CARD_RANKS.index('10' if card[0] == '1' else card[0])


def values(hand: list[str]) -> set[int]:
    """Return the unique values of the hand
    :param hand: list[str] - The hand to evaluate
    :return set[int] - The unique values
    """
    return {card_rank(card) for card in hand}


def value_count(hand: list[str]) -> int:
    """Return the number of card values in the hand
    :param card: str = A string representing the card
    :return int - The number of unique card values found in the hand
    """
    return len(values(hand))


def is_straight_flush(hand: list[str]) -> bool:
    """Return `True` if the hand is a straight fluch (all same suit with sequential
    values)
    :param hand: list[str] - The hand to evaluate
    :return bool - Whether the hand is a straight flush
    """
    if not all(card[-1] == hand[0][-1] for card in hand):
        return False
    return is_straight(hand)


def is_four_of_a_kind(hand: list[str]) -> bool:
    """Return `True` if the hand is four of a lind (at least four of the same suit)
    :param hand: list[str] - The hand to evaluate
    :return bool - Whether the hand is four of a kind
    :note - Takes advantage of the hand being sorted by value, which implies, if there are only
            two unique values, either the first one differs from the second or the last differs
            from the second-to-last
    """
    if value_count(hand) != 2:
        return False
    return card_rank(hand[0]) != card_rank(hand[1]) \
        or card_rank(hand[-1]) != card_rank(hand[-2])


def is_full_house(hand: list[str]) -> bool:
    """Return `True` if the hand is a full house (two of one value, three of another)
    :param hand: list[str] - The hand to evaluate
    :return bool - Whether the hand is a full hours
    :note - Takes advantage of the hand being sorted by value, which implies, if there are only
            two unique values, either the second card differs from the third or the third card
            differs from the fourth
    """
    if value_count(hand) != 2:
        return False
    return card_rank(hand[1]) != card_rank(hand[2]) \
        or card_rank(hand[2]) != card_rank(hand[3])


def is_flush(hand: list[str]) -> bool:
    """Return `True` if the hand is a flush (all same suit)
    :param hand: list[str] - The hand to evaluate
    :return bool - Whether the hand is a flush
    :note - Checks that the suite of all the cards matches the suit of the first card
    """
    return all([hand[0][-1] == card[-1] for card in hand])


def is_straight(hand: list[str]) -> bool:
    """Return `True` if the hand is a straight (sequential values)
    :param hand: list[str] - The hand to evaluate
    :return bool - Whether the hand is a straight
    """
    rank = card_rank(hand[0])
    for card in hand[1:]:
        curr_rank = card_rank(card)
        if curr_rank - 1 != rank:
            return False
        rank = curr_rank
    return True


def is_three_of_a_kind(hand: list[str]) -> bool:
    """Return `True` if the hand is a three-of-a-kind (three of one value, two others not of
    same value)
    :param hand: list[str] - The hand to evaluate
    :return bool - Whether the hand is a straight
    """
    if value_count(hand) != 3:
        return False


def is_two_pair(hand: list[str]) -> bool:
    """Return `True` if the hand is two pair (two of one value, two of another value, last of
    different value from pairs)
    :param hand: list[str] - The hand to evaluate
    :return bool - Whether the hand is a straight
    """
    if value_count(hand) != 3:
        return False


def is_one_pair(hand: list[str]) -> bool:
    """Return `True` if the hand is a pair (two of one value, three others not of duplicated
    values)
    :param hand: list[str] - The hand to evaluate
    :return bool - Whether the hand is a straight
    """
    pass


print(best_hands(["4D 5D 6D 7D 8D", "9D 5D 6D 7D 8D"]))
