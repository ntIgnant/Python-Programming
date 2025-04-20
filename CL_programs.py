from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="This program takes one argument 'str' and prints it in upper and lower case")

    # Add arguments for the CL program (Command Line Program)
    parser.add_argument('text', help="Text to convert")
    parser.add_argument('-u', '--uppercase', action='store_true', help="Flag to convert to uppercase")
    parser.add_argument('-l', '--lowercase', action='store_true', help="Flag to convert to lowercase")

    # Now, parse the arguments
    args = parser.parse_args()

    if args.uppercase:
        result = args.text.upper()  # convert the given text into uppercase
    elif args.lowercase:
        result = args.text.lower()  # convert the given text into lowercase
    else:
        print("Arguments missing. Use -u or -l")
        return  # Exit the function to avoid the print(result) line below

    print(result)

if __name__ == "__main__":
    main()