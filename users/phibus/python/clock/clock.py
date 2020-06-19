class Clock:
    def __init__(self, hour, minute):
        self.minute = minute % 60
        self.hour = (hour + minute// 60) % 24

    def __repr__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        h , m = minutes // 60, minutes % 60
        self.minute, self.hour = (self.minute + m) % 60, (self.hour + h + (self.minute + m) // 60) % 24
        return self

    def __sub__(self, minutes):
        h , m = minutes // 60, minutes % 60
        if m > self.minute:
            self.minute += 60 - m
            h += 1
        else:
            self.minute -= m
        self.hour = (self.hour - h) % 24
        return self