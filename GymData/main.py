from pathlib import Path
import csv

header = ["food,protein_g","carbs_g","fats_g","calories","price_per_unit","unit"] # Content of the first row of th exif file
csv_content = [
    [],
    [],
    [],
    []
]

with Path("DataBase.csv").open("wt") as csv_file:
    content = csv.writer(csv) # Create the writer csv object
    content.writerow(header) # write a single row (very fist row)
    content.writerows(csv_content) # Write the following rows (actual content)

print("Done, csv file Created!")

