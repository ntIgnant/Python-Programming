from pathlib import Path
import json

curr_wd = Path.cwd() # Current working directory

dir_path = Path("JsonDIR") # Directory of the target folder

absolute_path = curr_wd / dir_path # absolute path to the target folder

newJson = Path("kendrick_album.json")
file_path = absolute_path / newJson
file_path.touch() # Create the actual file

# Now, I'll edit the file

# Json data as string
json_content = json_str = '{"artist": "Kendrick Lamar", "album": "DAMN.", "release_year": 2017, "genres": ["Hip-Hop", "Rap"], "tracks": [{"title": "DNA.", "duration": "3:05"}, {"title": "HUMBLE.", "duration": "2:57"}, {"title": "LOYALTY.", "duration": "3:47"}]}'

album_data = json.loads(json_content) # json string parsing | 'loads' loeads a json string
# Parses a JSON-formatted string into a Python object (like a dictionary)

# write to the file
with file_path.open("wt") as file:
    content = json.dump(album_data, file, indent=4) # Dump = Takes a Python object and writes it into a file in JSON format

print(f"New file created in {file_path}!\n")

# Now, I'll print out the json data using ".load()" that comes with the json library
with file_path.open("rt") as f:
    data = json.load(f) # Correct way of printing out 'reading' a json file

# For better formating (just for the json file to have voter visual looking in the terminal)
print(json.dumps(data, indent=4))