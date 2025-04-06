def main():
    numbers = [input("Enter a Number: ") for _ in range(3)] # using list comprehension to create a list containing 3 input numbers

    # Unpackage the numbers
    num1, num2, num3 = numbers

    try:
        result = eval(f"{num1} * {num2} + {num3}") # evaluate the mathematical expression (as string)
        print(result)

    except (TypeError, NameError, SyntaxError) as err:
        print(f"There was an error with the type. {err}")


if __name__ == "__main__":
    main()