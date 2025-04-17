from pathlib import Path
import csv

# First I'll create the Class that represents the values of 'Person'
class Person:
    def __init__(self, name, date_birth, country):
        self.name = name
        self.date_birth = date_birth
        self.country = country

    def __str__(self):
        # class method to represent the values of 'Person'
        return (f"\nName:{self.name}\nDate Of Birth:{self.date_birth}\nCountry:{self.country}\n")

    def __eq__(self, other):
        return (self.name == other.name and self.date_birth == other.date_birth and self.country == other.country)


# Empty list to store all the people information
persons = []

# Now, I'll get the content from the csv file
file_path = Path("persons.csv") # Path of the file

with file_path.open("rt") as file:
    content = csv.DictReader(file)# creates a readable csv object

    for row in content:
        curr_person = Person(name=row["name"], date_birth=row["date of birth"], country=row["country"])

        # append the class instance (object) to the persons list
        persons.append(curr_person)

for p in persons:
    print(p)

print(persons[1] == persons[2]) # check for the equality '==' class method

# Find the oldest person in the csv file
ages = [per.date_birth for per in persons] # get the ages
# print(ages)

years = [pers[-4:] for pers in ages] # so this basically gets the last 4 characters
# print(years)

oldest_year = min(years)

print(f"Oldest Person was born in: {oldest_year}\n")

# Now I'll use lambda to get the oldest person (as the object itself)
super_old = min(persons, key=lambda p: p.date_birth)
print(f"The OLDEST guy: {super_old}")