my_list = [x for x in range(1, 11)]

number_str = "Number: "

number_list = [number_str + str(num) for num in my_list if num % 2 == 0] # list containing 'Number: x' for x if is even num

print(number_list)