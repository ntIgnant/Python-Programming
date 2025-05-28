import csv
from pathlib import Path as Pa

myCsvPath = Pa("to_dict_read.csv") # path to the csv file

with myCsvPath.open("rt") as file:
    reader = csv.DictReader(file) # create a reader object as a dictionary

    # for row in reader:
    #     print(row)

    dict_list = [dic for dic in reader]

    # print dict_list
    # for d in dict_list:
    #     print(d)

    for dictio in dict_list:
        print(dictio["First Name"], dictio["Final"], dictio["Grade"])

    filtered_pass = [dic["First Name"] for dic in dict_list if int(dic["Final"]) < 60]
    print(filtered_pass)

    # For each student, calculate the average grade
    each_average = [(diction["First Name"], ((int(diction["Test 1"]))+(int(diction["Test 2"]))+(int(diction["Test 3"]))+(int(diction["Test 4"]))) / 4) for diction in dict_list]
    print(each_average)

# Write a new CSV file called high_achievers.csv containing only students with an average score ≥ 85.
# Include: First Name, Last Name, Final, Grade, Average Score

# Create the new file
cwd_pa = Pa.cwd() # current working directory path

newFile_path = cwd_pa.joinpath("high_achievers.csv") # Create the path object
newFile_path.touch() # Create the actual empty file

# Access the file in write text mode to insert the header

header_data = ["First Name", "Last Name", "Final", "Grade", "Average Score"]

with newFile_path.open("w+", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header_data) # Create an object for the header
    writer.writeheader() #actually write the header values
    print(f"Header file values successfully added to {newFile_path.name}")

# Now, open up the 'old' csv file and fetch the data
csv_source_path = Pa("to_dict_read.csv") # Create the Path object to the csv

