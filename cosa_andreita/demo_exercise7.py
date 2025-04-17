# Get the input from user
while True:
    try:
        letter_range = int(input("Write an int (1 - 26): "))
        steps = int(input("Write an int: "))

        if letter_range in range(1, 27):
            break
        else:
            print("Invalid Input, try again\n")

    except ValueError:
        print("Invalid Input (Type), try again")

# All the letters from the alphabet
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
       "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

stations = []
for i in range(letter_range):
    stations.append(abc[i])  # just another way of appending (can be done with range() as well)

# Print stations (based on input val)
print("Train Stations: ")
for st in stations:
    print(st, end="")
print()  # or newline '\n'

# Initialize variables
curr_position = 0
direction = 1  # 1 -> forward | -1 -> backward

ends_counter = 0  # counter for the times that the train reaches 5 steps

pattern = []  # empty list to fill with the 'stop' letter when 5th stop is reached

# Append the first word and format the new value of steps (steps - 1)
pattern.append(stations[curr_position])
fixed_steps = steps - 1  # Corrected to steps-1

while ends_counter < 5:
    for _ in range(fixed_steps):
        curr_position += direction

        # Check if end is touched
        if curr_position == 0 or curr_position == len(stations) - 1:
            ends_counter += 1
            direction *= -1

    pattern.append(stations[curr_position])

print(f"Train Stop Sequence: {''.join(pattern)}")