def triplets_with_sum(number):
    buf = []
    limit = number // 2
    for i in range(1, limit):
        for j in range(i + 1, limit):
            k = number - i - j
            if k <= j:
                continue
            if i ** 2 + j ** 2 == k ** 2:
                buf.append([i, j, k])
    return buf


def is_triplet(triplet):
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2


if __name__ == '__main__':
    print(is_triplet((3, 4, 5)))
    print(triplets_with_sum(108))
