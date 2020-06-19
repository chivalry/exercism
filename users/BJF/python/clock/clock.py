class Clock:
    def __init__(self, hour, minute):
        corrected_mins = (hour * 60 + minute) % 1440 #total mins mod minutes in a day
        self.hour, self.minute = divmod(corrected_mins, 60)

    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)