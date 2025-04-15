# Hashable Stuff:
name = "Kit0"
hashed_name = hash(name)

age = 19
hashed_age = hash(age)

grade = 8.9
hashed_grade = hash(grade)

random_tuple = (1, 3, 4) # Tuples are immutable, so are hashable
hashed_tuple = hash(random_tuple)

# UNHASHABLE Stuff (mutable):
lista = [1, "ollow", 9.3, (1, 3)]
# print(hash(lista)) # THIS WILL CAUSE AN ERROR

diccionario = {"Oscar": 19, "Ray": 19, "Hasan": 90}
# print(hash(diccionario)) # this will rise an error as well


# How to hash mutable elements in python
# For Lists, convert it into a tuple
mi_lista = ["Ray", "Hassan", "Oscar", "Kit0"]

tupled_mi_lista = tuple(mi_lista)
print(tupled_mi_lista)
print(hash(tupled_mi_lista)) # This works fine, because the list was converted into a tuple (immutable content)

# For dictionaries, first we need to freeze the dictionary, and then it's hashable because it's immutable
mi_diccionario = {"Ray": 19, "Hassan": 90, "Oscar": 17, "Kit0": 0}
froz_dic = frozenset(mi_diccionario.items()) # This is the way of freezing a dictionary
print(froz_dic)
print(hash(froz_dic)) # Now, the hash will work because it's immutable now
