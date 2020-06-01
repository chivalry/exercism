class PhoneNumber:
    def __init__(self, number):
        param = number
        number = ''.join(([c for c in number[::-1] if c in '0123456789'][::-1]))
        if len(number) == 11 and number[0] != '1':
            raise ValueError('1 is only valid country code')
        if len(number) < 10:
            raise ValueError('Valid numbers have 10 digits')
        number = number[-10:]
        if number[0] in ['0', '1']:
            raise ValueError('Area codes cannot start with 0 or 1')
        self.number = number
        self.area_code = number[:3]
        self.exchange = number[3:6]
        if self.exchange[0] in ['0', '1']:
            raise ValueError('Exchange codes cannot start with 0 or 1')
        self.ext = number[6:]

    def pretty(self):
        return f'({self.area_code}) {self.exchange}-{self.ext}'


if __name__ == '__main__':
    print(PhoneNumber('+1 (613)-995-0253').number)
    print(PhoneNumber('613-995-0253').number)
    print(PhoneNumber('1 613 995 0253').number)
    print(PhoneNumber('613.995.0253').number)
    print(PhoneNumber('22234567890').number)
    print(PhoneNumber('+1 (223) 456-7890').number)
