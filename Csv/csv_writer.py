from pathlib import Path
import csv

curr_wd = Path.cwd()
# print(curr_wd)

newDir = Path("UselessDir")
newDir.mkdir(parents=True, exist_ok=True) # Create the new directory

final_path = curr_wd / newDir
# final_path = curr_wd.joinpath(newDir) # THis Is exactly the same as curr_wd / newDir, so all goodieeee

new_csv = final_path / "NewCsv.csv"
new_csv.touch() # Create an empty file 'NewCsv.csv'


header = ["Student", "ID", "Class", "GPA"]

with Path(new_csv).open("wt") as file:
    content = csv.DictWriter(file, fieldnames=header) # Creates the csv object as Dictionary (with its header values)
    content.writeheader() # This is for the first line (the header content)
    content.writerow({"Student": "Ignacio", "ID": "1133", "Class": "CS", "GPA": "3.2"}) # This can be written as a Dictionary

with new_csv.open("rt") as f:
    contenido = csv.reader(f) # Create a readable csv object

    for row in contenido:
        print(row) # print all the rows