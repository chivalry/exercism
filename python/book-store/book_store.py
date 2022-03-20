COST = 800
DISCOUNTS = [0.95, 0.9, 0.8, 0.75]


def build_buckets(basket):
    buckets = {book: 0 for book in range(1, 6)}
    for book in basket:
        buckets[book] += 1
    return buckets


def build_groups(buckets):
    groups = []
    for i in range(1, 6):
        loc_buckets = buckets.copy()
        group = []
        while any(elem > 0 for elem in loc_buckets.values()):
            count = 0
            for j in range(1, i+1):
                count += buckets[j] > 0
                loc_buckets[j] -= 1
            group.append(count)
            if loc_buckets[j] == 0:
                break
        groups.append(group)
    return groups


def total(basket):
    buckets = build_buckets(basket)
    groups = build_groups(buckets)
    return groups


if __name__ == '__main__':
    print(total([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]))
    print(total([1]))
