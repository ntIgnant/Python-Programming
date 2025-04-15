from pathlib import Path


curr_wd = Path.cwd() # current working directory path

newDir = Path("week15_material")
newDir.mkdir(parents=True, exist_ok=True) # this creates the actual new directory

full_path = curr_wd / newDir # Join the directory to the current working directory path

# Now, I'll create the new file with some information to hash3
file_path = full_path / "hashMe.txt"
file_path.touch() # creates the actual empty file

# Now I'll edit the file (add content)

with file_path.open("wt") as file:
    file.write("HashMePlease")

print("New file created and modified, NEEDS TO BE HASHED!")

# Now, I'll open up the file, store it's content int a variable, adn the hash the content

with file_path.open("rt") as f:
    content = f.read()
    my_message = content


print(f"Obtained content: {my_message}")

# Now, I'll hash it
hashed_message = hash(my_message)
print(hashed_message)

# Now, are two same strings, after the hash, equal?
fake_message = "HashMePlease"
hashed_fake_message = hash(fake_message)

# This is to verify if the two messages are 'the same'
if hashed_message == hashed_fake_message:
    print(True)
else:
    print(False)