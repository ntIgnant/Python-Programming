encoded_num = "1O 87l2022O Ol12231"
encoded_num = encoded_num.replace(' ', '')
# print(encoded_num)

decodification = {"O": "0", "l": "1"}

for char in encoded_num:
    for key, value in decodification.items():
        if char == key:
            encoded_num = encoded_num.replace(char, value) # .replace() needs to be used with an '=' to store the new string somewhere, as .replace returns a new string

print(encoded_num)
decoded_num = encoded_num

# get the average (counting a number from 0 to 9)
num_len = len(encoded_num)
# print(num_len) # get the length of the number

sum = 0
for num in decoded_num:
    sum += int(num)

# print(sum) # Sum of all the numbers

avrg = sum / num_len
print(avrg)