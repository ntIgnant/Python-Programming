from pathlib import Path
import csv

def separator():
    print("-" * 20)

with Path("tmp_csv_file.csv").open("rt") as file: # 'rt' stands for 'read - text mode'
    content = csv.reader(file) # use the csv .reader() to read the content as csv format

    for row in content:
        print(row[0:3]) # this will print row[0], row[1], and row[2] (ROW 3 EXCLUSIVE)

    separator()

# As Each instance of opening the file is a unique one, two read operations cannot be performed at the same time
# For example, in a .open() instance, .reader() and .DictReader() cannot be performed in the same .open() instance
with Path("tmp_csv_file.csv").open("rt") as f:
    contenido = csv.DictReader(f) # use the csv .DictReader() to read the content of the file as a Dictionary Object

    for r in contenido:
        print(r["ID"], r["Student"])

    separator()