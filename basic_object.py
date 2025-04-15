class Person:
    def __init__(self, name, age, height, country="Germany"):
        self.name = name
        self.age = age
        self.height = height
        self.country = country

    def __repr__(self):
        print(f"-DATA-\nName:{self.name}\nAge:{self.age}\nHeight:{self.height}\nCountry:{self.country}")

    # This is the 'same' as __repr__ but more for user interface (same thing ngl)
    def __str__(self):
        print(f"-DATA-\nName:{self.name}\nAge:{self.age}\nHeight:{self.height}\nCountry:{self.country}")

    def year_earnings(self, months, monthly_payment):
        return(months * monthly_payment)


newPerson = Person("Oscar", 17, 1.65, "Ecuador")
newPerson.__repr__() # Dunder or (MAGIC) methods can be called like this, but it's not pythonic
print(repr(newPerson)) # CORRECT WAY of calling dunder Methods (magic methods)

newPerson.__str__()
print(str(newPerson))  # CORRECT WAY of calling dunder Methods (magic methods)

newPerson_yearEarnings = newPerson.year_earnings(12, 2200)
print(f"Yearly Earnings: {newPerson_yearEarnings}")