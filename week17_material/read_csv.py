import csv
from pathlib import Path

csv_file_path = Path("grades.csv")

with csv_file_path.open("rt") as f:
    # rows = f.readlines() # TODO Replace with csv reader
    rows = csv.reader(f) # This will create a csv reader object

    # for row in rows:
    #     print(row)

# GET THE AVERAGE
with csv_file_path.open("rt") as file:
    # content = csv.reader(file) # creates a new csv object, I cannot use the previous one because the reader is gonna be 'empty' after I read it using the 'for loop'

    # NOTE! 'content' is an iterator, so once the data stored in the variable is read, it gets 'empty'
    # To 'reuse' the content of the iterator, I need to store it in a list or something that is reusable

    content = csv.DictReader(file)



    data = [row for row in content] # Store dictionary of the content of the students in a list
    total_students = len(data) # get the total number of students (basically the length of the list of dictionaries, because it skips the header)

    # print(data)
    print(f"Total Students: {total_students}")

    # Average = total_sum_grades / total_students
    total_sum_grades = 0
    for student in data:
        if "Final" in student:
            final_grade = student["Final"].strip()
            # print(f"Adding: {final_grade}") # this is for debugging
            total_sum_grades += float(final_grade)

    average_grade = total_sum_grades / total_students
    print(f"Average Grade: {average_grade}")


    # If I work from inside the context manager 'with.....as', I can still read/write or whatever to the file
    # Also, after everything the file will be closed safely

# Print the names of all students which achieved more than 60% in the fourth test
with csv_file_path.open("rt") as file:
    contenido = csv.DictReader(file) # creates a csv DictReader Object (iterable!)

    print(f"\nStudents that scored more than 60%: ")

    for estudiante in contenido:
        if "Test4" in estudiante:
            if float(estudiante["Test4"]) > 60:
                print(estudiante["First name"])
