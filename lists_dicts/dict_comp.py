# For dictionary comprehension, the key and value should be specified
# Structure:
# some dict = {key_expr: value_expr for item in iterable if condition}

#1.)
# squares = {1: 1, 2: 4, 3: 9}
# now, using dictionary comprehension
squares = {x: x**2 for x in range(1, 4)}
print(squares)

#2.)
# grades = {"Alice": 85, "Bob": 58, "Charlie": 95, "David": 62}
# ➡️ Keep only students who passed (score >= 60)
grades = {"Alice": 85, "Bob": 58, "Charlie": 95, "David": 62}
pass_students = {key: value for key, value in grades.items() if value >= 60}
print(pass_students)

#3.)
# words = ["apple", "banana", "cherry", "fig"]
# ➡️ Goal: Create a dictionary where each word is the key and its length is the value.
words = ["apple", "banana", "cherry", "fig"]
dict_words = {w: len(w) for w in words}
print(dict_words)

#4.)
# numbers = {"a": 1, "b": 2, "c": 3, "d": 4}
# ➡️ Goal: Create a new dictionary that only includes keys with even values.
numbers = {"a": 1, "b": 2, "c": 3, "d": 4}

even_dict = {key: val for key, val in numbers.items() if val % 2 == 0}
print(even_dict)

#5.)
# text = "hello"
# ➡️ Goal: Create a dictionary mapping each index to its character in the string.
text = "hello"
mapeo = {i: char for i, char in enumerate(text)}
print(mapeo)

#6.)
# grades = {"Alice": 91, "Bob": 76, "Charlie": 84, "David": 67}
# ➡️ Goal: Create a new dictionary where values are replaced with letter grades (A, B, C, D, F) based on this scale:
# 90+ → 'A'
#
# 80–89 → 'B'
#
# 70–79 → 'C'
#
# 60–69 → 'D'
#
# below 60 → 'F'
grades = {"Alice": 91, "Bob": 76, "Charlie": 84, "David": 67}

# Ni por el putas nos toman esto
letter_grades = {
    name: (
        'A' if score >= 90 else
        'B' if score >= 80 else
        'C' if score >= 70 else
        'D' if score >= 60 else
        'F'
    )
    for name, score in grades.items()
}
