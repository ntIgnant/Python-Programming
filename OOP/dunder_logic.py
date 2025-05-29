class Grades:

    # Initialize the class instance (blueprint)
    def __init__(self, exam1, exam2, exam3, exam4):
        self.exam1 = exam1
        self.exam2 = exam2
        self.exam3 = exam3
        self.exam4 = exam4

    # Declare __str__, it will return the string version of the data whenever 'print' is called
    # If __str__ is not declared, it would print the memmory address where the instance 'myGrades' is located
    def __str__(self):
        return f"{self.exam1}, {self.exam2}, {self.exam3}, {self.exam4}"

    # define __eq__ to do logical equivalence comparisons between CLASS INSTANCES
    # Whenever a class instance omparision is calling '==', '__eq__' will be executed
    def __eq__(self, other):
        return self.exam1 == other.exam1 and self.exam2 == other.exam2 and self.exam3 == other.exam3 and self.exam4 == other.exam4

myGrades = Grades(80, 80, 29, 78)
hisGrades = Grades(80, 80, 29, 78)

print(myGrades)

# Test comparison '=='
print(myGrades.exam1 == 80) # So, this works withou the magic method

# So, magick methods are basically to 'do things' between instance attributes
print(myGrades.exam1 == myGrades.exam2) # This also work because it is a 'numeric' comparison between instance attributes

# BUT THIS WOULD NEE DA __eq__ MAGIK LOGICAL METHOD
print(myGrades == hisGrades) # This should print a memory address instead (without the __eq__ dunder method)