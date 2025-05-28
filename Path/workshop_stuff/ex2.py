import csv
from pathlib import Path

# Determine the average over the final scores. (of grades.csv)

csv_file_path = Path("grades.csv")

with csv_file_path.open("rt") as file:
    reader = csv.reader(file)

    # IMPORTANT | CREATE A COPY OF THE ITERABLE FOR REUSAGE
    copy_reader = [row for row in reader] # create a copy to avoid integration exhaustion
    # In iterables, once it was iterated, it cannot be iterated again because the content
    # is already 'finished'
    # So, a copy must be created in order to access the content again

    str_finals = [row[-2] for row in copy_reader]
    print(str_finals)

    # Transform the values into integers
    int_finals = [float(val) for val in str_finals]

    finals_average = sum(int_finals) / len(int_finals)
    print(f"The average grade of the finals is: {finals_average}")

# • Print the names of all students which achieved more than 60% in the fourth test.
    students_passing = [row[1] for row in copy_reader if float(row[-3]) >= 60]

    print(students_passing)

# • For each student that achieved a B- or better, print their name together with their scores over all tests
# and the final exam.

    all_students_overall = {row[1]: sum(row[3:8]) / 4 for row in copy_reader} # [3:8]

    # print the dictionary with the student names and the overall scores
    for key, val in all_students_overall.items():
        print(f"{key}: {val}")

