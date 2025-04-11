from collections import Counter
from pathlib import Path

# message = "hola, esta es una prueba para contar es estar pruebaa"
#
# word = "es"
#
# counter = message.count(word)
# print(counter)
import collections

from pyasn1.debug import Printer

# word_list = ["cat", "dog", "dog", "dog", "dog", "cat", "cow", "cow", "lion", "fish"]
# random_str = "jabsdfhabshdfdkoewncmkugyaxcpoqiouiqgwermdenajsd"
#
# word_count = Counter(word_list)
# char_count = Counter(random_str)
#
# print(word_count)
# print(char_count)

# Testing == vs 'is'

# bool_result =  1 == 1
# print(bool_result) # this will return 'True' because the actual value is the same, is like comparing
# # the character 'a' with the same character 'a', it doesn't depend on the variable, just the actual value
#
# num_list = [1, 2]
# num_list2 = [1, 2]
#
# bool_result2 = num_list is num_list2
# print(bool_result2) # this will return 'False' because the actual variables (lists) are
# # different ones, even though they contain exactly the same values

# Creating a directory for fun :p

# curr = Path.cwd() # Current working directory Path
#
# newDir = Path("GymData")
# newDir.mkdir(parents=True, exist_ok=True) # Create the folder in the current working directory
#
# full_path = curr / newDir # Join the current working directory and the new created directory
#
# new_csv_file = full_path / "DataBase.csv"
# new_csv_file.touch() # Create the actual new csv file
#
# new_python_file = full_path / "main.py"
# new_python_file.touch() # Create the actual new python file (empty file)
#
# print(f"Two Files have been created '{new_csv_file}' and '{new_python_file}'!")

# Now, I'll just create a folder from here for fun "fun"

#
# curr_dw = Path.cwd() # Current working directory path
#
# newDir = Path("DataStructures")
# newDir.mkdir(parents=True, exist_ok=True) # Creates the actual directory
#
# absolute_path = curr_dw / newDir # Join the new folder into the current working directory
#
# # Now, I'll create an empty python file to do a LinkedList
# newFile = Path("SinglyLinkedList.py")
# absolute_file_path = absolute_path.joinpath(newFile) # Join the new file (same as: absolute_file_path =  absolute_path / newFile)
# absolute_file_path.touch() # This creates the actual empty file
# print(f"Python file '{newFile}' Created!")

