class Allergies:
    allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                 'tomatoes', 'chocolate', 'pollen', 'cats']

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return bool(self.score & (2 ** (self.allergies.index(item))))

    @property
    def lst(self):
        return [allergy for allergy in self.allergies if self.allergic_to(allergy)]
