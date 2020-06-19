COST = 800
DISCOUNTS = [0.95, 0.9, 0.8, 0.75]


def total(basket):
    basket.sort()
    return basket


if __name__ == '__main__':
    print(total([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]))
