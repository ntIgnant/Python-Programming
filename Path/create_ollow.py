from pathlib import Path

cwd = Path.cwd() # current working directory path

file_path = cwd.joinpath("ollow.txt") # create the file_path object
file_path.touch() # create empty file

# Open the file and write something
with file_path.open("w") as f:
    content = f.write("Hello?")

    # This should be closed automatically
    print(f"File created in {file_path.name}")
