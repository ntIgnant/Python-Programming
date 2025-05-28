from pathlib import Path

my_path = Path(input("Please enter a directory: "))

# check if the input direcoty exists
if not my_path:
    print("Direcotry not found")
    exit()

else:
    new_dir_name = input("Enter new Direcoty name: ")
    
    new_dir_path = my_path / new_dir_name # append the new folder name
    new_dir_path.mkdir() # create the new directory
    print(f"Done!, '{new_dir_path}' created!")

    dir_path = new_dir_path

    new_file_name = input("Now, enter the name for a txt file (.txt): ")
    new_file_name += ".txt" # add the .txt termination
    dir_path = dir_path / new_file_name
    dir_path.touch()
