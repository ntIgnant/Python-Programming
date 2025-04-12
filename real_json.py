from pathlib import Path
import json
file_path = Path("JsonDIR/real_json.json") # path of the target json file

with file_path.open("rt") as file:
    content = json.load(file) # load the json content to print it out

# print(json.dumps(content, indent=4)) # print out the content with nice formating (just for good looking)

# Print just specific stuff
print(f"{content['userID']}, {content['id']}")