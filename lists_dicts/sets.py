num_list = [x for x in range(10)]
num_set = {z for z in range(10)} # set comprehension
num_tuple = (y for y in range(10)) # tuple comprehension wtf

# print(num_list, num_set)

my_str = "I like Sets and sets And dictionaries"
my_str = my_str.lower().split() # .split() alone just creates a copy, so that copy needs to be stored somewhere

my_set = {word for word in my_str}

my_list = []

for index, word in enumerate(my_set):
    my_list.append(f"{index + 1}. {word}")

print(my_list)