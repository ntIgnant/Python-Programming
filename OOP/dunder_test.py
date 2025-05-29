class Person:

    # Initialize the blueprint for the class
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"{self.name}, {self.age}, {self.height}"

persona1 = Person("Zigz", 17, 1.90) # initialize a class instance (object) from Person

print(persona1.name) # This works because an individual element of the instance is being accessed
print(persona1) # This will print the memory address of where the instance is located | MAGIK METHOD NEEDED

