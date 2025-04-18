from collections import Counter
from pathlib import Path
# import pytorch # As this library is not built in python, I need to install it externally using pip (or pip3) install pytorch

# message = "hola, esta es una prueba para contar es estar pruebaa"
#
# word = "es"
#
# counter = message.count(word)
# print(counter)
import collections


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

# # I'm just gonna create a python file to practice this pathlib shit
#
# folder_path = Path("week15_material")
# file_path = folder_path / "comprehension.py"
# file_path.touch() # Creates the actual new empty file
# print(f"New file create din {file_path}")

# # Another useless and completely unnecessary creation of a file from python
# folder_path = Path("week15_material")
# file_path = folder_path / "DataStruct_choice.py"
# file_path.touch() # Creates the emtpy file

# # Just another file creation
#
# absolute_path = Path("week18_material")
# file_path = absolute_path.joinpath("persons.py")
# file_path.touch() # creates the actual empty file
# print(f"New file created in '{file_path}'")

# # another file creation
# cwd_path = Path.cwd()
#
# file_path = cwd_path / "assertion_basics.py"
# file_path.touch() # creates the empty file