# List comprehension is literally creating lists in a compacted way

# So I'm just going to convert stuff into list comprehension way
# 1.)
# squares = []
# for x in range(10):
#     squares.append(x ** 2)

squares = [x ** 2 for x in range(10)]
print(squares)

# 2.)
# evens = []
# for x in range(20):
#     if x % 2 == 0:
#         evens.append(x)
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

#3.)
# words = ["apple", "banana", "cherry"]
# uppercased = []
# for word in words:
#     uppercased.append(word.upper())
words = ["apple", "banana", "cherry"]
uppercased = [word.upper() for word in words]
print(uppercased)

# 4.)
# pairs = []
# for x in range(5):
#     pairs.append((x, x ** 2))
pairs = [(x, x ** 2) for x in range(5)]
print(pairs)

# 5.)
# matrix = [[1, 2, 3], [4, 5, 6]]
# flat = []
# for row in matrix:
#     for num in row:
#         flat.append(num)
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

#6.)
# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
square = [num**2 for lista in matrix for num in lista if num **2 > 10]
print(square) # It is partially wrong


#7.) This is SET comprehension
sentences = ["hello world", "python is fun", "list comprehension is cool"]
uniqueLen = {len(word) for each in sentences for word in each.split()}
print(uniqueLen)

