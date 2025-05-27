# Unpacking refers to extract values from a collection (list, dictionary, tuple)
packed = [[0, "a"], [1, "b"], [2, "c"], [3, "d"]]

# Use list comprehension to create list with the unpacked values
indices = [index for index, char in packed]
chars = [char for index, char in packed]

print(indices, chars)

for i, content in enumerate(packed):
    print(f"{i+1}. list{content}")

# Another packing example
compacted = [i for i, _ in packed] # using list comprehension, this list will contain the 'num values'
                                   # that are in 'packed'
print(compacted)


