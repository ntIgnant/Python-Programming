num1 = 10
num2 = 22

assert num1 + num2 == 32 # This doesn't return anything, because it is a True assertion
# assert num1 + num2 == 30 # This returns an assertionError, because num1 + num2 != 30
assert num1 + num2 == 30, "This answer should be 32" # This will rise an assertionError message

# Assertions can be disabled in the execution with the flag '-O', assertions are for debugging mainly
# Assertions are NOT USED to validate user input

print(num1 + num2)