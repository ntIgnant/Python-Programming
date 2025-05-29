from pathlib import Path
import json

students = [
    { "name": "John", "grade": 80.2 },
    { "name": "Lea", "grade": 100.0 }
]

# I'll create a file, and I'll dump the data into a specific section of the json data

my_file_path = Path("Some_Jsons").joinpath("dumped.json")
my_file_path.touch() # Create an empty file 'dumped.json'

# Open the file with context manager and dump string content plus (object) content
with my_file_path.open("wt") as file:
    json.dump({
        "course": "LZSCC.1111",
        "students": students
    }, file, indent=4)

    print(f"String data AND object data was successfully dumped into {my_file_path.name}!")