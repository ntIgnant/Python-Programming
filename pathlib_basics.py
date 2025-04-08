from pathlib import Path


# ----- Useful Paths -----
# Current Directory
curr_dir = Path.cwd()
# Home Directory | Note: The default home directory will be different between linux/macOs and Windows
home = Path.home()


# ----- Creating and Listing Directories -----
new_dir = Path("newdir_test") # directory containing a child (subfile)
new_dir.mkdir(parents=True, exist_ok=True) # Create the folder if it doesn't exist

file_path = new_dir / "ollow.txt" # create a new file (txt) inside the new directory
file_path.write_text("ollow world\n") # write content inside the created file

# create the full path (starting from the current working directory)
full_path = curr_dir / file_path
print(full_path)
