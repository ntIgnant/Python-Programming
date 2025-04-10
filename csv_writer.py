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
    content = csv.writer(file) # Creates writable csv object
    content.writerow(header) # Write a single row (first one for the header)
    content.writerows({"Student": "Ignacio", "ID": "1133", "Class": "CS", "GPA": "3.2"}) # This can be written as a Dictionary

with