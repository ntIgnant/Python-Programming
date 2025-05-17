from pathlib import Path
import json

cwd_path = Path.cwd() # Current working directory path

newDir = Path("JsonDIR")
newDir.mkdir(parents=True, exist_ok=True) # Creates the actual new directory

final_path = cwd_path.joinpath(newDir) # Same as saying "final_path = cwd_path / newDir"

# Now, I'll create an empty JSON file inside the directory
newJson = Path("first_json.json")

newFile = final_path.joinpath(newJson) # same as newFile = final_path / newJson
newFile.touch() # Creates the actual empty file

# Now, I'll edit the fill to add basic JSON stuff

json_str = '{"Name": "Kit0", "Age": 19, "Country": "Ecuador", "Dead": "false"}' # Basic JSON content 'Dictionary like'
data = json.loads(json_str) # Writes the content as a JSON object


with Path(newFile).open("wt") as file:
    json.dump(data, file, indent=4)