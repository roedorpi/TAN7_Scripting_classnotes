"""
WORKING WITH FILES

## open() function
one argument: which file to open file must be located in the same folder as the script you are editing otherwise, file path must be included

pyton assigns the object (the opened file)  to file_object the keyword "with" closes the file once access is no longer needed:
this means we do not need to use close() function later

the .read() method reads the content of the entire file into a string.
"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# alternative:

myFile = open('pi_digits.txt')
contents = myFile.read()
myFile.close() # close file when no longer using it

print(contents)

"""
Reading lines one by one.

The file object is iterable and a for loop will take a new line at each iteration.  
"""
# read file in line by line:

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# make a list of lines from file using .readlines() with out a for loop.

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())

"""
## working with file content

# build a single string that contains all the digits in the file, no whitespaces:

"""
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))

"""
## large files: one million digits
"""
##
import os

curdir = os.getcwd()
filename = os.path.join(curdir, "csvfiles","cats.csv")

with open(filename) as file_object:
    lines = file_object.readlines()
##
pi_string = '' 
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string}...")
print(len(pi_string))


## is your birthday contained in pi?

#birthday = input("Enter your birthday, in the form ddmmyy: ")

birthday = "200789"

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


"""
## WRITING FILES

write to an empty file:
"""
filename = 'programming.txt'

with open(filename, 'w') as file_object: 
    file_object.write("I love programming.")

""" 
The open function automatically opens files in read-only mode.
 if the file you are opening doesn't exist, open function will create it. 
 
 open in:
 'r' - read mode
 'w' - write mode
 'a' - append mode
 'r+' - read and write mode
 
 careful! if you open a file with 'w' mode, and the file already exists, python will erase all contents of that file!
"""
## writing multiple lines:

filename = 'programming.txt'

with open(filename, 'w') as file_object: # w means write mode
    file_object.write("I love programming.\n")
    file_object.write("I am so happy I am studying Python.\n")


filename = 'programming.txt'

with open(filename, 'a') as file_object: # a means append,  write to the end of the file don't erase contents
    file_object.write("This is the greatest course at AAU.\n")
    file_object.write("TAN FOREVER.")


## handling missing files error

filename = 'alice.txt'

with open(filename) as f:
    contents = f.read()

filename = 'alice.txt'

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
##
"""
## file object attributes
When the Python open() function is called, it returns a file object called a file handler. Using
this file handler, you can retrieve information about various file attributes.

file_handler.closed  returns a Boolean True if the file is closed or False otherwise.

file_handler.mode  returns the access mode with which the file was opened.

file_handler.name  returns the name of the file.
"""

# in the code below, file_handler is a variable name and can be substituted for anything
# such as "potato"
# so then it would be potato.name, potato.closed, and potato.mode

file_handler = open("pi_digits.txt", 'w')
print(f"File name is {file_handler.name}")
print(f"File State is {file_handler.closed}")
print(f"File Opening Mode is {file_handler.mode}")


"""
## analyzing text

file source: https://www.gutenberg.org/ebooks/11

You can download the plain text file and use the .split() method to generate a list of words

"""
##
title = "Alice in Wonderland"
title.split() # splits by spaces


filename = 'wonderland.txt'
# files can be saved with different encodings, that is different ways to map symbols to ascii code,
# you have probably experienced this when opening a file from a different language or operating system,
# where special characters are shown wrong. The open function allows you to specify the encoding of the file.
with open(filename, encoding='utf-8-sig') as f:
    contents_lines = f.readlines()
    contents = f.read()
    words = contents.split()
    num_words = len(words)

print(f"the file {filename} contains approx. {num_words} words.")
##
for i in range(0, len(contents_lines)-1,2):
    print(contents_lines[i])
    print(contents_lines[i+1])
##
"""
## CSV files
a csv file (comma separated values file) is a plain text file that uses specific structure to arrange
tabular data. Meaning: each piece of data is separated by a delimiter (a comma, a tab, a colon, 
or a semi-colon), and then when we parse the file, we read the delimiter as a character separating data 
(often into tables). each row returned by the reader is a list of string elements containing the data 
found by removing the delimiters.
"""
##
import os
import csv

curdir = os.getcwd()
filename = os.path.join(curdir, "csvfiles","birthdays.csv")

with open(filename, mode='w', newline="") as my_csv:
    csv_writer = csv.writer(my_csv, delimiter=';')
    csv_writer.writerow(["Name", "Birthday", "Cake"])
    csv_writer.writerows([["jesus", "24/12/0", "apple cake"], ["Mohammed", "29/10/570", "brownies"], ["Dalai Lama", "6/7/1935", "rice cake"]])

##
with open('birthdays.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(f"\t{row[0]}'s birthday is in {row[1]}, and his/her favorite cake is {row[2]}.")
            line_count += 1
    print(f'Processed {line_count} lines.')


### reading csv files into a dicitonary


with open('birthdays.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    col_names = csv_reader.fieldnames
    line_count = 0
    for row in csv_reader:
        if line_count == 0: # the first line in the file is assumed to contain keys
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f"\t{row[col_names[0]]}'s birthday is in {row[col_names[1]]}, and his/her favorite cake is {row[col_names[2]]}.")
        line_count += 1
    print(f'Processed {line_count} lines.')


##
import csv

with open('cats.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',', fieldnames=['name', 'color', 'adj']) # when first line is not keys
    line_count = 0
    csv_reader.restkey()
    print(f'Column names are {", ".join(csv_reader.fieldnames)}')
    for row in csv_reader:
        print(f"\t{row['name']} is a {row['color']} cat who is simply {row['adj']}.")
        line_count += 1
    print(f'Processed {line_count} lines.')
##
"""
## writing csv files
using writer object and .write_row() method
"""
import csv

with open('vegetables.csv', mode='w', newline='') as veggie_file: # why newline=''? 
    veggie_writer = csv.writer(veggie_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # quotechar: if I want to include delimiter character as data, I need to put it in this character
    # quoting: 
    # csv.QUOTE_MINIMAL - only quote fields if they contain the delimiter or the quotechar (default)
    # csv.QUOTE_ALL - every field is wrapped in quotes
    # csv.QUOTE_NONNUMERIC - quote text fields, convert all numeric fields to floats
    
    veggie_writer.writerow(['vegetable','color','taste','goes well with'])
    veggie_writer.writerow(['carrot', 'orange', 'sweet',"potatoes, peas"])
    veggie_writer.writerow(['potato', 'brown', 'neutral','literally everything'])

"""
 ## writing csv files from a dictionary
"""
##
import time as tt
import datetime as dt
import csv
import os
curdir = os.getcwd()
filename = os.path.join(curdir, "csvfiles","fruit.csv")

with open(filename, mode='a', newline='') as csv_file:
    fieldnames = ['fruit', 'color', 'taste', 'time']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'fruit': 'banana', 'color': 'yellow', 'taste': 'delicious','time':tt.time()})
    writer.writerow({'fruit': 'apple', 'color': 'red', 'taste': 'meh','time':tt.time()})
    writer.writerow({'fruit': '', 'color':'', 'taste':'','time':tt.time()})



# note: we will be revisiting csv files when we get to the pandas library
##
"""
### fun with input() and writing files!
"""
import csv

with open('TAN7.csv', mode='w', newline='') as csv_file:
    fieldnames = ['student name', 'rubber duck name', 'favorite snack', 'birthday month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writing_active = True
    while writing_active:
        name = input('What is your name? ')
        duck = input("what is your duck's name? ")
        snack = input("what is your favorite snack? ")
        month = input("What is your birthday month? ")
        writer.writerow({fieldnames[0]: name, fieldnames[1]: duck, fieldnames[2]: snack, fieldnames[3]: month})
        repeat = input("Would you like to add another person? (y/n) ")
        if repeat == 'n':
            writing_active = False



import csv

with open('TAN7_other.csv', mode='w', newline='') as TAN7_file: # why newline=''? 
    TAN7_writer = csv.writer(TAN7_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    TAN7_writer.writerow(['student name', 'rubber duck name', 'favorite snack', 'birthday month']) # our headers
    
    writing_active = True
    while writing_active:
        name = input('What is your name? ')
        duck = input("what is your duck's name? ")
        snack = input("what is your favorite snack? ")
        month = input("What is your birthday month? ")
        TAN7_writer.writerow([name, duck, snack, month])
        repeat = input("Would you like to add another person? (y/n) ")
        if repeat == 'n':
            writing_active = False

