import datetime


class Clock:
    def __init__(self, hour, minute):
        hour += minute//60
        self.hours = hour % 24
        self.minutes = minute % 60
        self.time = datetime.time(self.hours, self.minutes)

    def __repr__(self):
        return self.time.strftime("%H:%M")

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(self.hours, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(self.hours, self.minutes - minutes)
