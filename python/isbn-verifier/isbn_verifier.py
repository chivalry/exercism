def is_valid(isbn):
    isbn = [c for c in isbn if c != '-']
    if any([c not in '0123456789X' for c in isbn]):
        return False
    isbn = [10 if i == 'X' else int(i) for i in isbn]
    if len(isbn) != 10:
        return False
    if 10 in isbn and isbn.index(10) != 9:
        return False
    return sum([isbn[i] * (10 - i) for i in range(10)]) % 11 == 0


if __name__ == '__main__':
    print(is_valid('3-598-21X08-X'))
