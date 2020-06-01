import threading


class BankAccount:
    STATE_CLOSED = 0
    STATE_OPEN = 1

    def __init__(self):
        self.balance = 0
        self.state = self.STATE_CLOSED

    def get_balance(self):
        if self.state == self.STATE_CLOSED:
            raise ValueError('account is closed')
        return self.balance

    def open(self):
        if self.state == self.STATE_OPEN:
            raise ValueError('cannot open an open account')
        self.state = self.STATE_OPEN
        self.balance = 0

    def deposit(self, amount):
        if self.state == self.STATE_CLOSED:
            raise ValueError('account is closed')
        if amount < 0:
            raise ValueError('cannot deposit negative amount')
        self._adjust_balance(amount)

    def withdraw(self, amount):
        if self.state == self.STATE_CLOSED:
            raise ValueError('account is closed')
        if amount < 0:
            raise ValueError('cannot withdraw negative amount')
        if amount > self.balance:
            raise ValueError('cannot overdraw account')
        self._adjust_balance(amount * -1)

    def close(self):
        if self.state == self.STATE_CLOSED:
            raise ValueError('cannot close closed account')
        self.state = self.STATE_CLOSED

    def _adjust_balance(self, adjustment):
        self.balance += adjustment
