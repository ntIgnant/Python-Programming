import logging
from pathlib import Path

log = logging.getLogger(__name__) # Logger defined before class so it can be used

class File:
    '''
    This class will store two parameters, 'name' and 'info'.

    It will also have 2 class methods (functions)L
    - Create a file with the given name in the current directory
    - Add the string info to the file

    :)
    '''

    def __init__(self, name, info_str):
        self.name = name
        self.info_str = info_str

        self.file_path = None # This will be filled with the actual file path after its creation


    def __str__(self):
        return f"Name:{self.name}\nInfo String:{self.info_str}"

    def createFile(self):
        '''
        This function is going to create the empty file in the current directory
        '''

        cwd_path = Path.cwd() # current working directory path
        file_path = cwd_path.joinpath(self.name) # creates the empty file with the given name
        file_path.touch() # create the actual empty file

        self.file_path = file_path # add it as a class variable to be (global)

        log.info(f"File CREATED") # this si for the log, just to keep track of the actions of the workflow

    def addInfo(self):
        '''
        This function is going to add the given information (infoString) into the file
        '''

        with Path(self.file_path).open("wt") as file:
            content = file.write(f"{self.info_str}\n") # write the give string into the file (newline terminated)

        log.info("Information WRITTEN to the file") # info for the log, to keep track of what's going on


def main():
    file_name = str(input("Enter a Name for the File: "))
    file_info = str(input("Enter anything: "))

    log.info("File Name and Info Str OBTAINED") # this si information that will appear in the log, it's to keep track of what's going on

    file = File(file_name, file_info) # object created
    file.createFile() # create file
    file.addInfo() # write into the file


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
