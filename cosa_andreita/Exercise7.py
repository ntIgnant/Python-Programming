
#Esta parte hace lo que le pido jajaja
# =============================================================================
# while True:
#     letters = int(input("Write an integer number between 1 and 26: "))
#     steps = int(input("Write an integer number : "))
#     if letters <= 26:
#         break
#     
#     else:
#         print("Invalid input. Pleas try again")
#         print("")
# # all the letters from the alphabet 
# abc=["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M","N","O", "P", "Q", "R", "S", "T", "U", "V", "W","X", "Y", "Z"]
# 
# stations =[] # is going to save just the ammount of letters the user selects and print them
# for i in range(letters):
#     stations.append(abc[i])
#     
# print("The train stations are:")
# for x in stations:
#    print(x, end=" ")
# =============================================================================


#Esto en teoría es el prpgrama completo
# print("The train stations are:")
#Una parte fue sugerida por  Chat GPT, pero igual ni me da el output correcto


while True: 
    letters = int(input("Write an integer number between 1 and 26: "))
    steps = int(input("Write an integer number: ")) 
    if letters <= 26:
        break
    else:
        print("Invalid input. Please try again")
        print("")

# All the letters from the alphabet 
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
       "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Build list of stations
stations = []
for i in range(letters):
    stations.append(abc[i])

print("The train stations are:")
for x in stations:
    print(x, end=" ")
print("\n")

# Initialize variables
position = 0  # Start at A
direction = 1  # 1 = forward, -1 = backward
ends_touched = 0
sequence = stations[position]  # First station

while ends_touched < 5:
    for _ in range(steps - 1):  # Already counted the current as first step
        # Move one step
        position += direction

        # Check if end is touched
        if position == 0 or position == letters - 1:
            ends_touched += 1
            direction *= -1  # Reverse direction

    sequence += stations[position]

print("Train sequence:", sequence)
