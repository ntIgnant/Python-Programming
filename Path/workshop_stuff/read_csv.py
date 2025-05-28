from pathlib import Path
import csv

with Path('grades.csv').open("rt") as f:
    reader = csv.reader(f)

    # this is for debugging only (to read the content)
    for row in reader:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
