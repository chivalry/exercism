class Luhn:
    def __init__(self, card_num: str):

        spaces_discarded = "".join(card_num.split())
        card_digits = [int(d) for d in card_num if d.isdigit()]
        double_every_second_digit = [
            2 if (i - 1) % 2 == 0 else 1 for i in range(len(card_digits))
        ]
        products = [
            i[0] * i[1] for i in zip(reversed(card_digits), double_every_second_digit)
        ]
        total = sum(product - 9 if product > 9 else product for product in products)

        self.is_valid = (
            len(card_digits) == len(spaces_discarded)
            and len(card_digits) > 1
            and total % 10 == 0
        )

    def valid(self) -> bool:
        return self.is_valid
