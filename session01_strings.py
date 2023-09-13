"""
STRINGS
definition: a string is a series of characters inside "" or '' quotes

"""
"this is a string."
'this is also a string.'
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
""""It isn't," she said."""

#strings can also be variables:

string1 = "this is a string."
str(5)

# concatenation
"Alek" + "sandra"
"""
changing case in a string with methods
definition: a method is an action that python can perform on a piece of data

the "." tells python to make the title() method act on the variable name

every method is followed by a set of parentheses (), because methods often need additional 
information to do their work and that information is provided inside the parenthesis

the title() function doesn't need additional information, so the parentheses are empty

useful if you do not trust the capitalization that your users provide

"""
nameLower = "aleksandra kaszowska"
nameUpper = "ALEKSANDRA KASZOWSKA"
print(nameLower.title())
print(nameUpper.title())

print(nameLower.upper())
print(nameUpper.lower())
"""
using variables in strings
f-string: to insert a value into a string, place the f letter immediately before opening the quote
"""
firstName = "aleksandra"
lastName = "kaszowska"
fullName = f"{firstName} {lastName}"
print(fullName)
print(f"Hello, {fullName.title()}!")
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
fullName = f"{firstName} {lastName}"
print(f"Hello, {fullName.title()}!")

"""
whitespace: any nonprinting character (spaces, tabs, end of line symbols, etc.) that can be 
used to organize outputs
"""
# tabs: \t
print("chips")
print("\tchocolate")

# new line in a string: \n
print("Favorite snacks:\nchips\ncookies\nchocolate")

# or combine
print("Favorite snacks:\n\tchips\n\tcookies\n\tchocolate")

#temporary stripping whitespace:

favoriteSnack = ' cookies '

favoriteSnack.rstrip() # stripping whitespace from the right side
favoriteSnack.lstrip() # stripping whitespace from the left side
favoriteSnack.strip() # stripping whitespace from both sides
# permanently removing whitespace requires associating the stripped value with variable name:

favoriteSnack = ' cookies '
favoriteSnack = favoriteSnack.strip()

# you can use more than one method
favoriteSnack = favoriteSnack.strip().upper()
"""
getting to parts of strings
finding length of a string:
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetLength = len(alphabet)
print(alphabetLength)
"""
we can refer to specific characters in the string by calling on their position

the position of a character is usually denoted by first calling on the string variable, then the position in [ ]

in Python, forward addressing starts at 0, while backward addressing starts at -1

this means that if we are counting from left to right, the first character of the string occupies position 0, the second character occupies position 1, and so on.

0 1 2 3 4 5 6 7 8 9 10 11...
A B C D E F G H I J K  L  M N O P Q R S T U V W X Y Z
if we are counting from right to left, the last character of the string occupies position -1, the second to last character occupies position -2, and so on

A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
                                                 ...-5 -4 -3 -2 -1
move the 6th character of "alphabet" into a variable called "letter":
"""
letter = alphabet[6]
print(letter)

# put the last and first character of alphabet into a variable using len():

last = alphabet[len(alphabet)-1]
print(last)

first = alphabet[-len(alphabet)]
print(first)

"""
string slicing
we can refer to substrings of our string using slicing (cutting parts of the string)

the "cursor" positions for slicing:

    -9   -8   -7   -6   -5   -4   -3   -2   -1
s =    A    B    C    D    E    F    G    H    I
     0    1    2    3    4    5    6    7    8    9
"""
s = "ABCDEFGHI"
print(s[1:5])
print(s[0:-3])
print(s[-8:0])
print(s[:])
print(s[-9:9])
print(s[::2])

p = "The youngest pope was 11 years"
x = p.split()
y = f"{x[-2]} {x[2]}s"
# y = x[-2] + " " + x[2] + "s" # alternative string assembling

print(y)

fullName = "ALEKSANDRAKASZOWSKA"
firstName = fullName[:10] # leaving the first one empty means "start from the beginning"
lastName = fullName[10:] # leaving the second one empty means "go through to the end"

print(firstName, lastName)


"""
changing elemenents in strings
strings are immutable, meaning: once created, we cannot change the elements within the string

to change a string, we need to make a new string:
"""
name = "Aleksandra"
nameUSA = name[0:3]+"x"+name[5:10]

#nameUSA = f"{name[0:3]}x{name[5:10]}" # alternatively

print(name)
print(nameUSA)