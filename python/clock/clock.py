class Clock:
    MAX_HRS = 24
    MAX_MINS = 60

    def __init__(self, hour, minute):
        time = hour * self.MAX_MINS + minute
        self._time = time % (self.MAX_MINS * self.MAX_HRS)
        self.hours = self._time // self.MAX_MINS
        self.minutes = self._time % self.MAX_MINS

    def __repr__(self):
        return f'{self.hours:02d}:{self.minutes:02d}'

    def __eq__(self, other):
        return self._time == other._time

    def __add__(self, minutes):
        return Clock(0, self._time + minutes)

    def __sub__(self, minutes):
        return Clock(0, self._time - minutes)
