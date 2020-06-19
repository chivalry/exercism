class Clock:
    MAX_HRS = 24
    MAX_MINS = 60

    def __init__(self, hour, minute):
        time = hour * self.MAX_MINS + minute
        self._time = time % (self.MAX_MINS * self.MAX_HRS)

    def __repr__(self):
        hours, minutes = divmod(self._time, self.MAX_MINS)
        return f'{hours:0>2}:{minutes:0>2}'

    def __eq__(self, other):
        return self._time == other._time

    def __add__(self, minutes):
        return Clock(0, self._time + minutes)

    def __sub__(self, minutes):
        return Clock(0, self._time - minutes)
