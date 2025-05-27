import random

# Tuples:
#   Pairs, or more numbers that are immutable (cannot be modified)
#   Tuples are not sets, so they have an order and therefore and index

# Sets:
#   Sets have no oder (math definition) so they cannot be accessed though random access 'aka index'
#   But sets can be 'modified', a value can be added into a set

# Example Tuple:
myTup = (1, 2, 3)

print(myTup[0]) # tuples have random access because they have an order
print(myTup[::-1]) # list slicing is allowed in tuples (e.g reverse print)

# But set's are inmmutable, cannot be modified
# myTup += 3 # this does't work
# print(myTup)

# Example Sets:
# this is just to show that sets have no order
mySet = {x for x in random.sample(range(10), 5)} # set containing 5 random numbers from 0 to 10 (exclusive)

print(mySet)

# as sets have no order, they don't have random access either
# print(mySet[0]) # this won't work

# but set's can me 'modified' add and remove stuff
print(0 in mySet) # verify content inside the set

mySet.add(22)
print(mySet)

numProg = [1, 3, 5, 2, 6, 4, 6, 1]
newset = set(numProg)
print(newset)

