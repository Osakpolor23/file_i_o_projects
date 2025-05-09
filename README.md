# File I/O Operations in Python: Handling Text, CSV, and Images  

## **Overview**  
File input and output (I/O) operations are essential for working with data stored in files as it gives the assurance of continuity, instead of the outputs being lost as the program closes.

This repository contains multiple Python programs that handle different types of file processing, from reading and writing text files to transforming CSV data and manipulating images. Each script is designed to perform a ***specific file operation***, demonstrating the use of key Python libraries such as `csv`, `tabulate`, and `Pillow`.  

Throughout this project, I implemented functions that efficiently process structured data, ensuring robustness while handling edge cases gracefully.

## **Programs Breakdown**  

### **1️⃣ lines.py – Counting Lines of Code in a Python File** 

This script counts the number of lines of code in a ***Python file***, while excluding comments and blank lines.  

**Functionality:**  

    - Reads the file given as a command-line argument.  
    - Strips leading/trailing whitespace from each line.  
    - Ignores lines that are empty or start with `#` (comments).  
    - Outputs the total count of code lines.  

**Usage:**  

    $python lines.py script.py

**✅ Example Output:**

    14 (Lines of actual code in script.py)

### **2️⃣ pizza.py – Converting a CSV Pizza Menu into an ASCII Grid**

This script takes a CSV file containing a pizza menu and formats it into an ASCII table using the tabulate package.

**Functionality:**

    - Reads a CSV file specified via the command line.

    - Extracts headers dynamically for flexible processing.

    - Converts CSV rows into a structured ASCII table for readability.

    - Displays the pizza menu in a neatly formatted grid.

**Usage:**

    $python pizza.py sicilian.csv

**✅ Example Output:**

    +------------------+---------+---------+
    | Sicilian Pizza   | Small   | Large   |
    +==================+=========+=========+
    | Cheese           | $25.50  | $39.95  |
    +------------------+---------+---------+
    | 1 item           | $27.50  | $41.95  |
    +------------------+---------+---------+
    | 2 items          | $29.50  | $43.95  |
    +------------------+---------+---------+

### **3️⃣ scourgify.py – Cleaning and Transforming CSV Data**

This script reads a CSV file with raw data, restructures the field names, and writes the cleaned version into a new file.

**Functionality:**

    - Accepts two command-line arguments:

        input.csv (original raw CSV file)

        output.csv (new cleaned CSV file)

    - Reads data using csv.DictReader().

    - Splits full names into "first" and "last" fields.

    - Writes structured data into a new CSV file with organized headers.

**Usage:**

    python scourgify.py raw_data.csv cleaned_data.csv

**✅ Example Output (cleaned_data.csv):**

    first,last,location
    Blessing, Asabomaka, The Alapere
    Titola,James,The Ikotun

### **4️⃣ shirt.py – Overlaying an Image onto Another**

This script applies an overlay (shirt image) onto another image while ensuring proper resizing and transparency.

**Functionality:**

    - Accepts two arguments:

        input_image (the base image)

        output_image (the final processed image)

    - Reads the input image using Pillow.

    - Resizes the input image to match the overlay (shirt.png).

    - Ensures transparency handling for accurate layering.

    - Saves the transformed image in the specified output file.

**Usage:**

    python shirt.py photo.jpg edited_photo.jpg

✅ Produces an image with the "shirt.png" overlay.

Feel free to fork this repository, submit pull requests, or suggest additional test cases to improve coverage.