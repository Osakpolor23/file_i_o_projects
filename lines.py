# import sys and os
import sys # to take in command line arguments
import os  # to perform splitting and test existence of file

# Ensure the right command line arguments are entered.
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# define the validate_file function to validate input files
def validate_file(filename):
    # split into the file name and extension
    name, extension = os.path.splitext(filename)
    # remove case sensitivity and strip the leading dot
    extension = extension.lower().strip(".")  # os.path.splitext returns the extension with the leading dot
    # check if the extension is valid
    if extension.lower() != "py":
        sys.exit("Invalid file extension--must be a python file")

    return name, extension

# ensure the command line args must be 2(file name inclusive)
if len(sys.argv) == 2:
    # assign the input to a variable
    file = sys.argv[1]  # The input file to modify

    # validate file
    name, extension = validate_file(file)

    # # check if the file exists in the directory
    # if not os.path.exists(file):
    #     sys.exit(f"{file} doesn't exist")

# create a counter to count each valid line of code
counter = 0

try:
    with open(f"{file}") as input_file:
        # loop through each line in the file
        for line in input_file:
            # avoid counting blank lines(empty lines with whitespaces) and comments -- lines starting with #
            if line.strip() != "" and not line.lstrip().startswith("#"):
                # increment the counter if the two conditions are met
                counter += 1            
# handle non file existence error
except FileNotFoundError:
    sys.exit(f"{file} doesn't exist")

# output the number of lines of code
print(counter)