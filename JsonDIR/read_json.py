from pathlib import Path
import json

# First, I'll create a new json file, and I'll dump a specific string for the content

file_path = Path("Some_Jsons").joinpath("nuevo.json")
file_path.touch() # Create the actual new empty file 'nuevo.json'
print(f"New file created. '{file_path.name}'")

# Open the empty file and write the content (as string) using context manager

with file_path.open("wt") as file:
    json.dump({
        "object": "fine_tuning.job.event",
        "id": "ftevent-abc123",
        "created_at": 1677610602,
        "level": "info",
        "message": "Created fine-tuning job"
    }, file, indent=4)

    print(f"Data dumped into {file_path.name}!")


# Now, open the same file to read the content, also with context manager
with file_path.open("rt") as f:
    reader = json.load(f)

    print(reader)