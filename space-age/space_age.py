class SpaceAge:
    SECS_PER_YEAR = 31557600

    def __init__(self, seconds):
        self.earth_age = seconds / 31557600

    def _round(self, number):
        return round(self.earth_age / number, 2)

    def on_earth(self):
        return self._round(1)

    def on_mercury(self):
        return self._round(0.2408467)

    def on_venus(self):
        return self._round(0.61519726)

    def on_mars(self):
        return self._round(1.8808158)

    def on_jupiter(self):
        return self._round(11.862615)

    def on_saturn(self):
        return self._round(29.447498)

    def on_uranus(self):
        return self._round(84.016846)

    def on_neptune(self):
        return self._round(164.79132)
