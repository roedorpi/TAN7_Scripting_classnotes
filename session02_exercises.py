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

userName = input("Hello, what is your name? ")

# print a compliment about their name
print(f"{userName.title()} is such a lovely name!")

# ask the user to input their weekend plans
weekendPlans = input(f"So {userName.title()}, what are your plans for the weekend? ")

# print a message about the weekend plans being fun, regardless of their input
print("That sounds like so much fun!")

# ask the user about their favorite color
favColor = input("What is your favorite color? ")

# print a message complimenting that specific color
print(f"{favColor.title()} is my favorite too.")

# print a message explaining that you will ask the user for two numbers
print("Let's play a game. Give me two numbers and I will add them!")

# ask the user to input the first number, and convert that number to integer right away
equation1 = int(input("first number: "))

# ask the user to input the second number, and convert that number to integer right away
equation2 = int(input("second number: "))

# calculate sum of two numbers
sumBoth = equation1 + equation2


# print the answer
print(f"The sum of {equation1} and {equation2} is {sumBoth}!")

# use the function eval() to evaluate a mathematical expression.
# look up the use of the function on the python documentation
eq_literal = input('Write a math equation that Python can understand: ')
eq_result = eval(eq_literal)

print(f"The result is: {eq_result}.")

# print a farewell message
print("Thank you for talking to me, and have a nice day!")


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

# inside the previous while loop, write another while loop to decide what happens when the user gives the undesirable
# rating to your product

# ask the user if they want to input another review, and if not - switch the flag from off.
print("Welcome to the product rating program.")
user_data = []
collecting_data = True
while collecting_data:
    name = input('What is your name? ')
    product = input("what is the product? ")
    rating = int(input("what is your rating, out of 5? "))
    while rating <= 3:
        rating = int(input("are you sure? try rating again, out of 5: "))
    comments = input("any other comments? ")
    user_data.append([name, product, rating, f"{comments}"])
    repeat = input("Would you like to add another person? (y/n) ")
    if repeat == 'n':
        collecting_data = False

print("Thanks for participating!")
print(user_data)
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
# once your code works, you come back to this cell and convert your variables into input() remember that input function
# always returns a string! also remember that your user might want to put a later date as the first input, and an
# earlier date as the second input you need to tell users exactly what to do, otherwise they will do silly things that
# can mess up your code
leap_years = set(range(1700, 2500, 4)) - {1700, 1800, 1900, 2100}
days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

date1 = input('Enter a date in the format DD MM YYYY: ')
date2 = input('Enter a second date in the format DD MM YYYY: ')

# find out which date is earlier
numdate1 = []
numdate2 = []
for i in date1.split(): numdate1.append(int(i))
for i in date2.split(): numdate2.append(int(i))

# compare years
if numdate1[2] < numdate2[2]:
    first_date = numdate1
    second_date = numdate2
elif numdate1[2] > numdate2[2]:
    first_date = numdate2
    second_date = numdate1
else: # it is the same year lets compare the months
    if numdate1[1] < numdate2[1]:
        first_date = numdate1
        second_date = numdate2
    elif numdate1[1] > numdate2[1]:
        first_date = numdate2
        second_date = numdate1
    else: # same month lets compare the days
        if numdate1[0] < numdate2[0]:
            first_date = numdate1
            second_date = numdate2
        elif numdate1[0] > numdate2[0]:
            first_date = numdate2
            second_date = numdate1
        else:
            print("You entered the same date twice!")
            first_date, second_date = numdate1

## calculate how many days from the first date to the end of that year.
first_to_endofyear = 0

#days to the end of the month
first_to_endofyear += days_in_months[first_date[1]-1] - first_date[0]

#full months to the end of the year
for month in range(first_date[1], 12):
    first_to_endofyear += days_in_months[month]

if first_date[1] <= 2 and first_date[2] in leap_years:
    first_to_endofyear += 1

## calculate how many days from the second date to the beginning of that year.
second_to_startofyear = 0

# days to the start of the month
second_to_startofyear += second_date[0]

# full months to the start of the year
for month in range(0, second_date[1]-1):
    second_to_startofyear += days_in_months[month]

if second_date[1] <= 2 and second_date[2] in leap_years:
    second_to_startofyear += 1

## How many days are in the full years in between the two dates
years_btw = set(range(first_date[2]+1,second_date[2]))
leap_years_btw = leap_years.intersection(years_btw)
in_between = int(len(years_btw)*365) + int(len(leap_years_btw))

## Calculate total sum
if first_date[2] != second_date[2]:
    how_many_days = first_to_endofyear + second_to_startofyear + in_between
else:
    how_many_days = second_to_startofyear + first_to_endofyear - 365
