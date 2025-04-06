import def_main_extfile as hello

def main():
    userName = input(str("Enter a Name: "))
    hello.helloName(userName) # execute the greeting with the new name and the function of the other file
    exit()

if __name__ == "__main__":
    main()