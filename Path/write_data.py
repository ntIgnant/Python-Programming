from pathlib import Path as Z
import csv

# First create the new csv empty file
cwd_path = Z.cwd() # Current working directory path

newFilepath = cwd_path / "nuevo.csv" # Create the new
newFilepath.touch() # Create the actual empty file

# Header data
header_data = ["Name", "Age", "Country"]

# raw data
data = [
    ["Zigs", 19, "Ecuador"],
    ["Oscar", 17, "Espania"],
    ["Nestor", 18, "Venezuela"]
]

with newFilepath.open("w", newline="") as file:
    # Write the header line
    file.write(",".join(header_data) + "\n")

    # Write each row
    for list in data:
        file.write(",".join(map(str, list)) + "\n")

# Check the content of the NEW csv file
with newFilepath.open("rt") as f:
    reader = csv.DictReader(f)

    for dic in reader:
        print(dic)
