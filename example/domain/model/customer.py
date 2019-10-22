from datetime import date

class Customer():

    def __init__(self, id, name, birth_date):
        self.id = id
        self.name = name
        self.birth_date = birth_date

    def check_mininum_age(self, minimum_age):
        age = self._calculate_age()
        if age >= minimum_age:
            return True
        return False

    def _calculate_age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        