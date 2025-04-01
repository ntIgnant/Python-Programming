# Basic 'enumerate' function

# my_string = "Hello"
#
# enumerated_list = []
#
# for item in enumerate(my_string):
#     enumerated_list.append(item)
#
# print(enumerated_list)

user_str = input(str("Enter Something: "))
user_str.split()

enumerated_list = [item for item in enumerate(user_str)] # same shit but using list comprehension
print(enumerated_list)