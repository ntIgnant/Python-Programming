def Sum(num1, num2):

    '''
    This function returns the arithmetic sum of two numbers
    '''

    result = num1 + num2
    return result

def Sub(num1, num2):

    "This Function returns the arithmetic subtraction of two numbers"

    result = num1 - num2

    "??????? THIS IS NOT GONNA BE PRINTED OUT BY __doc__"

    return result

def Mult(num1, num2):
    result = num1 * num2
    return result

resultado = Sum(10, 20)
assert resultado == 30 # this will return True, so no assertionError

# The function 'help()' basically prints out everything that is in between quotations inside a function

help(Sum) # 'Request'/Print the documentation of the function 'Sum'
help(Sub) # 'Request'/Print the documentation of the function 'Sub'
help(Mult) # This can also be requested for documentation, but it has nothing inside it

print(resultado)