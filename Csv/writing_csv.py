from pathlib import Path
import csv

from urllib3.filepost import writer

# Create the header file of the csv
header = ["Item", "Amount", "Price"]

# Create the data for the csv (based on the header of course)
data = [
    ["Milk", "3", "2.7"],
    ["Banana", "10", "5.34"],
    ["Water", "2", "2.7"],
    ["Bred", "10", "3.8"]
]

# If the path is not specified before, the file will be created in the current directory by default
file_path = Path("food_items.csv")

with file_path.open("wt") as file:
    content = csv.writer(file) # this initializes the csv writer object
    content.writerow(header) # Writes a single csv row. Ths is the first row, so it needs to be the header
    content.writerows(data) # write the rest of the rows, which is the data

print(f"The file '{file_path}' was successfully created!")

