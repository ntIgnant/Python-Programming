SIZE = 10

def read_numbers():
	numbers = []

	for _ in range(SIZE):
		try:
			number = int(input("Enter a NUmber: "))
			numbers.append(number)

		except ValueError:
			print("Wrong Tye, try again")

	return numbers


l = read_numbers()
print(" ".join(str(i) for i in l))
