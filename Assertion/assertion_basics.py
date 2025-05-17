# -Basic assertion example-

num = 10

# If this assertion is fine, nothing happens, but of it's false, it throws an AssertionError
assert num > 5 # this will pass just fine, but with the opposite sign '<' it will result in an Error

# The error message can also be customized
newNum = 7
example_num = 3

assert newNum < example_num, "This is BAD bro..." # <assertion> statement, error message

# Example DEBUGGING
