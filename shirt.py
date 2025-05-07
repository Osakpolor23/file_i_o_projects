# import the pillow library, sys and os
from PIL import Image
from PIL import ImageOps
import sys
import os

# Ensure the right command line arguments are entered.
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

def validate_file(filename):
    # split into the file name and extension
    name, extension = os.path.splitext(filename)
    # remove case sensitivity and strip the leading dot
    extension = extension.lower().strip(".")  # os.path.splitext returns the extension with the leading dot
    # create a list of the valid extensions 
    valid_extension = ["jpg", "png", "jpeg"]

    # check if the extension is valid
    if extension not in valid_extension:
        sys.exit("Invalid input")

    return name, extension
   
# ensure the command line args must be 3(file name inclusive)
if len(sys.argv) == 3:
    # assign the inputs to variables
    file1 = sys.argv[1]  # file to write into i.e modify
    file2 = sys.argv[2]  # file to output i.e save as
    # validate files
    name_1, extension_1 = validate_file(file1)
    name_2, extension_2 = validate_file(file2)

     # check if the input file exists in the directory
    if not os.path.exists(file1):
        sys.exit(f"Input file {file1} doesn't exist")
    
    # check if the file have the same extensions
    if extension_1 != extension_2:
        sys.exit("Input and output have different extensions")

# open the over-laying image
shirt = Image.open("shirt.png")
# get the image size and assign to sizd
size = shirt.size   # comes as a tuple -- (600, 600) in this case

# open the input image
input_image = Image.open(file1)
# crop the input image to be the same size as the over-laying image
input_image = ImageOps.fit(input_image, size)
# call the .paste() method to modify the image in place
input_image.paste(shirt, (0,0), mask = shirt)  # assign shirt to mask to keep transparency of over-laying shirt

# save the modifications as output file
input_image.save(file2)

# Also used in the command prompts during scripting are:
# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
# -- to download over-laying shirt
# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip 
# -- to download zipped file containing muppets to be used as inputs
# sudo apt install zip -- to install zip command to my wsl environment
# unzip muppets.zip -- to unzip the zipped file to get the muppets input images to modify