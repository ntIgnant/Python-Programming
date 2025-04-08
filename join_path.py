from pathlib import Path

cwd_path = Path.cwd() # current working directory path

base = Path("test_parent")
base.mkdir(parents=True, exist_ok=True) # Creation of the actual directory

full_path = cwd_path / base

for i in range(3):
    tmp_file_path = full_path / f"file{i+1}.txt" # this will create multiple empty txt files from 1..3
    tmp_file_path.touch() # this is the actual creation of the file in the disk
    tmp_file_path.write_text(f"File No.{i+1}\n") # write something in each file

full_path = cwd_path / base
print(full_path)