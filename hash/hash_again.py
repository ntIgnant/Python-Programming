# So there are two main types of 'objects' in hashing
# hashable and unhashable objects

# If the object is mutable (can change) then it is unhashable
# If the object is immutable (cannot change) then it is hashable

name = "Zigz" # hashable object
num = 90 # aslo, hashable object BUT for integer the HASH IS THE SAME VALUE, because 90 (number) is already an identifier
float_num = 9.62343 # also hashable
tup = (1, 5, 2) # also, hashable, because it is immutable

# to hash something is basically to pass the immutable object thought a function
# that converts it into a number or set of random chars
print(hash(name), hash(num), hash(float_num), hash(tup)) # NOTE: the hash of num will be the same number, so 90


# For hashes, the hash of an object will always output the same hash value, so hashes can be compared and should match for the same value
a = "hola"
b = "hola"

print(hash(a) == hash(b)) # This returns true because the VALUE is the same, it does't matter that the values are different

diccionario = {1: "Oscar", 2: "Ignacio"} # this cannot be hashable because a dictionary is mutable

# But it can 'freez' and convert it into an immutable object
frozenDict = frozenset(diccionario) # Now, this dictionary is converted into a tuple (immutable obj)
print(frozenDict)

# So, now it can be hashed because it is a tuple
print(hash(frozenDict))