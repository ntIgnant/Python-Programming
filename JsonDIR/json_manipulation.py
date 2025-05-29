from pathlib import Path
import json

# Data to import to a new json file
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Analysis"],
    "is_active": True
}

# Create a new directory
cwd_path = Path.cwd() # current working directry
newJsondir = cwd_path / "Some_Jsons" # a 'joined path' object
newJsondir.mkdir(parents=True, exist_ok=True) # create the new directory | enable the options for parent and exist to avoid errors

# Access thr new directory and create a nre json file inside it
full_file_path = Path("Some_Jsons").joinpath("myjson.json")
full_file_path.touch() # Create the empty json file
print(f"New Json file created inside '{full_file_path.parent}' directory")

# Now, open the json file with context manager and load the values of 'data'

with full_file_path.open("wt", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

    print(f"'Data' added to {full_file_path.name}!")