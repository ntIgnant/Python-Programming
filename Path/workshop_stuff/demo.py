# There are two main lbraries for 'file management' in python, 'os' (old aproach and low level), and 'pathlib'(new hight level aproach)
# pathlib is object oriented

from pathlib import Path

# check if a path exists

my_path = Path(input("Please enter a path: "))

if not my_path.exists():
    print(f"The path '{my_path}' does not exist")

else:
    print("It does exist")
