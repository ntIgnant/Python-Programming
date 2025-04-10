from pathlib import Path
import csv

with Path("DataBase.csv").open("rt") as file:
    content = csv.reader(file) # Open up the csv file in read (text mode) as list (Normal) Reader

    for row in content:
        print(row)