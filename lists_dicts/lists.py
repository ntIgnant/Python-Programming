# my_list = [x for x in range(1, 11)]
# number_str = "Number: "
# number_list = [number_str + str(num) for num in my_list if num % 2 == 0] # list containing 'Number: x' for x if is even num
#print(number_list)

# a = []
# a += "123"
# print(a) # this should print the list containing just one value ["123"] | FALSE
#          # The result will be the same as saying list("123") -> ['1', '2', '3'] so convert all
#          # the elements into a list
#
# # Same as
# b = list("123")
# print(b) # re turbio
#
# # Repeating:
# # in python, we can print the elements of a list certain number of times
#
# print(3 * b) # this woul lead to -> ['1', '2', '3', '1', '2', '3', '1', '2', '3'] in a whole list

# lista = ['a', 'b', 'c', 'd']
#
# input_char = str(input("Please enter a char: "))
#
# if input_char in lista:
#     print(f"{input_char} is in {lista}")
# else:
#     print(f"The character {input_char} is not in the list")

# Some list utilities
int_lista = [2, 5, 1, 6, 3, 6, 9, 22]
char_lista = ["a", "b", "h", "r", "A", "P", "c", "C"]
str_lista = ["aa", "ab", "ah", "ccr", "aA", "eP", "fc", "zC"]


# 'Arithmetic' functions doesn't work on str lists, just in number lists (ints, floats, etc)
print(f"-Max values-\nMax int list: {max(int_lista)}")
print(f"-Min values-\nMin int list: {min(int_lista)}")
print(f"-Sum of elements-\nSum int list: {sum(int_lista)}")

# Basic sort
# 'sorted()' works with strings 'chars' as well
print(f"Sorted int list: {sorted(int_lista)}")
print(f"Sorted char list: {sorted(char_lista)}")
print(f"Sorted str list: {sorted(str_lista)}")