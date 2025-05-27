# 1.)
# words = ["apple", "banana", "grape", "kiwi", "peach"]

# uniqueVowels = (ch if ch in ["a", "e", "i", "o", "i"] for word in words for ch in word.split())
# print(uniqueVowels) # WRONG LA PUTA MADREEEEEEEEEEEEEEEEEEEEee

# # Basics of if statements in comprehension
# evens = []
# for x in range(10):
#     if x % 2 == 0:
#         evens.append(x)

evens = {x for x in range(10) if x % 2 == 0}
print(evens, type(evens))

# 2.)
# words = ["cat", "apple", "dog", "banana"]
# # Output: ['apple', 'banana']
words = ["cat", "apple", "dog", "banana"]
new_set = {word for word in words if len(word) > 3}
print(new_set)

#3.)
# items = ["apple", "", "banana", "", "cherry"]
items = ["apple", "", "banana", "", "cherry"]
no_empty_str = {word for word in items if word != ""}
print(no_empty_str)

#4.)
# From this list:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create a set of numbers that are divisible by 3 using set comprehension
div_by_3 = {num for num in nums if num % 3 == 0}
print(div_by_3)