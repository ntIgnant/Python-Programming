# Bulk operations is where sets really shine
# Bulk operations are operations done with collections (lists, sets, tuples, dictionaries)

mySet = {1, 8, 3, 6, 7, 8, 2}
myOtherSet = {1, 2, 4, 6}

print(mySet.intersection(myOtherSet)) # Find the intersection between two sets
print(mySet.union(myOtherSet)) # Union between two sets
print(mySet.difference(myOtherSet)) # Difference between mySet and MyOtherSet 'A \ B'


