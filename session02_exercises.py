"""
Problem 1.
write a chatbot program:

1) the program asks the user for their name, and then tells them it is a very pretty name
2) the program asks the user if they have any fun weekend plans, and then tells them it sounds like a lot of fun
3) the program asks the user what is their favorite color, and then responds that (the favorite color) is also the
   chatbot's favorite color
4) the program asks the user to write a math equation, and then provides the answer to that equation
5) the program thanks the user for the conversation and wishes them a nice day

"""
# Hints:

# assign variable names to input, and use those variables in fstrings in print input function always returns a string
# for the math question, you can only add integers (cannot add strings to each other)


"""
Problem 2.
Collecting user feedback (and manipulating user reviews)
Write code so users can rate their experience using a product.

The user needs to provide the following information: user name, product name, star rating, any other comments
BUT! the user should not able to give a rating lower than 4 or 5 stars; if the user inputs a rating of 3 or lower, your 
program will keep asking the user if they're sure, repeatedly, until the user inputs 4 or 5.
"""
# Hints
# Since this stops when a condition is met, we will be using a while loop, so start with setting up a flag

# Save data into a list of lists, with the information provided by the user

# inside the previous while loop, write another while loop to decide what happens when the user gives the undesirable rating to your product

# ask the user if they want to input another review, and if not - switch the stop flag.

"""
Problem 3. 
count days between two user-defined dates
write a script that calculates how many days are between two user-defined dates
confirm that your results are correct here: https://www.timeanddate.com/date/duration.html

PLEASE NOTE: if you google this challenge, you will find a very simple and elegant solution using datetime package. 
Try writing this script WITHOUT using datetime, and using your own logic and the programming knowledge you have from 
class. If you are having trouble putting this into code, try writing a flowchart of your algorithm

There will NOT be one correct answer to this challenge; the hints below are hints to the code I wrote, 
but there are more ways you can solve this problem.  
 
"""
# Hints:
## define assumptions ##
# a leap year occurs every 4 years except years 1700, 1800, 1900, and 2100
# different months have different durations

##program steps##
# ask user to specify two dates
# hint: when you are writing code, and troubleshooting it, you can define your own dates here
# this means that you define two dates that you want to use as variables, and then write the rest of your code
# once your code works, you come back and convert your variables into input(). Remember that input function always returns a string! also remember that your user might want to put a later date as the first input, and an earlier date as the second input you need to tell users exactly what to do, otherwise they will do silly things that can mess up your code.

leap_years = set(range(1700, 2500, 4)) - {1700, 1800, 1900, 2100}
days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
