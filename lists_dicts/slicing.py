# Some basic list slicing

myList = [1, 2, 3, 4, 5, 6, 7]
print(myList[1:5]) # this will print the list from index one to index 5 (exclusive) so from index 1 - 4

# REVERSE INDEXING
print(myList[::-1]) # this will print the list in reverse order (step = 1)
# for list slicing = [start : stop(exclusive) : step]

# REVERSE INDEXING
print(myList[:3]) # this will print from index 0 to index 3(exclusive)
print(myList[::-3]) # this will start the print from the last element (negative step) and will print the
                    # elements once every three steps

print(myList[:3:-1]) # this will print the elements in reverse indexing (starting from the last one)
                     # it will print the first 3 index elements (starting from the end)

# BULK OPERATIONS AND LIST SLICING
a = [1, 6, 4, 4, 5, 6, 7]
a[:3] = [1, 2, 3] # replace the indices of the slicing with specific ones
print(a)

someName = "oscar"
slicedName = someName[0::2] # this is like 'from 0 index, all the values each 2 steps'
                            # so slicedName = [o, c, r]

slicedName = " ".join(slicedName) # this just adds a ' ' (space) between characters
print(slicedName)


