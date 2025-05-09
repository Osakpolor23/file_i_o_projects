# import the tabulate package, csv, sys and os
import csv # to interact with the csv file
from tabulate import tabulate # to format as ASCII art
import sys # to take in command line arguments
import os  # to perform splitting and test for existence of file


# Ensure the right command line arguments are entered.
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

def validate_file(filename):
    # split into the file name and extension
    name, extension = os.path.splitext(filename)
    # remove case sensitivity and strip the leading dot
    extension = extension.lower().strip(".")  # os.path.splitext returns the extension with the leading dot
    # check if the extension is valid
    if extension.lower() != "csv":
        sys.exit("Invalid file extension--must be a csv file")

    return name, extension

# ensure the command line args must be 3(file name inclusive)
if len(sys.argv) == 2:
    # assign the inputs to variables
    file = sys.argv[1]  # The input file to modify

    # validate file
    name, extension = validate_file(file)

    # # check if the file exists in the directory
    # if not os.path.exists(file):
    #     sys.exit(f"{file} doesn't exist")

# create an empty list of pizzas to store data in memory
pizzas = []

# open the given csv file
try:
    with open(f"{file}") as input_file:
        # read the file with .DictReader() method in csv library
        reader = csv.DictReader(input_file)
        # get the column names dynamically usinf the DictReader attribute of .fieldnames
        field_names = reader.fieldnames # returns a list of the columnames
        
        # loop through each row in the file
        for row in reader:
            # append the values under the fieldnames of each row  in the correct order to the list
            pizzas.append([row[field_name] for field_name in field_names]) # extract values based on the fieldname order

except FileNotFoundError:
    sys.exit(f"{file} doesn't exist")

# assign the field_names list to the headers arg of the tabulate function
headers = field_names
print(tabulate(pizzas, headers, tablefmt="grid"))


# for this project, I did the following in the terminal prior to the scripting:
# created a virtual environment called file_i_o_env
#  to install the project's packages and dependencies e.g the tabulate package
# downloaded the two csv files (regular.csv and sicilian.csv) that hold the pizza menus using wget e.g
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv
