from pathlib import Path
import json

file_path = Path("kendrick_album.json") # File path

# Open the file with context manager and read some data using dict keys

with file_path.open("rt") as file:
    content = json.load(file) # So, content is a dictionary basically

    print(f"{content["artist"]}\n{content["tracks"]}")