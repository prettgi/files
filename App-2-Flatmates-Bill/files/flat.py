class Bill:
    """
    Class Bill represents the bill of the flat and includes the following attributes: amount, currency and period.
    """

    def __init__(self, amount, currency, period):
        self.amount = amount
        self.currency = currency
        self.period = period


class Flatmate:        
    """
    Class Flatmate defines the flatmates with their attributes: name, days_in_house. 
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        return bill.amount*weight
        