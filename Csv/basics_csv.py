from pathlib import Path
import csv


# First I'll fix the space in the csv file (I put a space after each comma bruh)
my_csv_file = Path("tmp_csv_file.csv")
content = my_csv_file.read_text() # read the content of the file

fixed_csv_file = content.replace(" ", "") # remove the spaces

my_csv_file.write_text(fixed_csv_file) # write the fixed content


with Path("tmp_csv_file.csv").open("rt") as f:
    reader = csv.reader(f)

    # print out the actual content of the csv file (the rows)
    for row in reader:
        # print(row) # all the content (all the rows)
        print(row[0], row[-1]) # specific content (just the first and last row)

# SEPARATOR ONLY
print('-' * 20)

# Read the csv file as a dictionary
with Path("tmp_csv_file.csv").open("rt") as file:
    file_reader = csv.DictReader(file)

    for r in file_reader:
        print(r["Student"], r["Class"]) # specify the values to be printed out with dictionary like style