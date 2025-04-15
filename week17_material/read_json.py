from pathlib import Path
import json

json_file_path = Path("users.json")

with json_file_path.open("rt") as file:
    content = json.load(file) # creates a json readable object

    # print(json.dumps(content, indent=4)) # print the json file with nice looking (with nice indentation shit)

    print(f"Users Online: ")
    for user in content:
        if user["online"] is True or user["online"] == "true":
            print(user["username"]) # Not working, WTF?
