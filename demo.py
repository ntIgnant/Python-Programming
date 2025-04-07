from collections import Counter

# message = "hola, esta es una prueba para contar es estar pruebaa"
#
# word = "es"
#
# counter = message.count(word)
# print(counter)
import collections

# word_list = ["cat", "dog", "dog", "dog", "dog", "cat", "cow", "cow", "lion", "fish"]
# random_str = "jabsdfhabshdfdkoewncmkugyaxcpoqiouiqgwermdenajsd"
#
# word_count = Counter(word_list)
# char_count = Counter(random_str)
#
# print(word_count)
# print(char_count)

# Testing == vs 'is'

bool_result =  1 == 1
print(bool_result) # this will return 'True' because the actual value is the same, is like comparing
# the character 'a' with the same character 'a', it doesn't depend on the variable, just the actual value

num_list = [1, 2]
num_list2 = [1, 2]

bool_result2 = num_list is num_list2
print(bool_result2) # this will return 'False' because the actual variables (lists) are
# different ones, even though they contain exactly the same values

