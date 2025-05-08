# import the csv library, sys and os
import csv # to interact with the csv file
import sys # to take in command line arguments
import os  # to perform splitting and test existence of file


# Ensure the right command line arguments are entered.
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


# ensure the command line args must be 3(file name inclusive)
if len(sys.argv) == 3:
    # assign the inputs to variables
    file1 = sys.argv[1]  # file to write into i.e modify
    file2 = sys.argv[2]  # file to output i.e save as

# check if the input file exists in the directory
if not os.path.exists(file1):
        sys.exit(f"Could not read {file1} ")

# create an empty list of students to store data in memory
students = []

# open the given csv file
with open(f"{file1}") as input_file:
    # read the file with .DictReader() method in csv library
    reader = csv.DictReader(input_file)
    # loop through each row in the file
    for row in reader:
        # extract the name and house
        full_name = row["name"]
        house = row["house"]
        # split the name into first_name and last_name
        last_name, first_name = full_name.split(",")
        # remove leading whitespaces
        first_name = first_name.strip()
        last_name = last_name.strip()
        # create a dictionary to store the three new data formats
        student = {"first_name": first_name, "last_name": last_name, "house": house}
        # append the dictionary to the list of students
        students.append(student)
  
# open the file to write into
with open(f"{file2}", "a") as output_file:
    # use .DictWriter() to write into the file so as to specify the fieldname structure
    writer = csv.DictWriter(output_file, fieldnames = ["first_name", "last_name", "house"])
    # write the header row
    writer.writeheader()
    # loop through each row in students
    for row in students:
        # write the rows by accessing each field in the list of dictionary
        writer.writerow({"first_name": row['first_name'], "last_name":row['last_name'], "house":row['house']})



# I downloaded the input csv file on the command line with:
# wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv