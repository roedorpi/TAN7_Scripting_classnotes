"""
CONDITIONAL TESTS

Definition: a conditional test allows you to check any condition of interest.
his means that at the heart of every if statement, there is an expression that
can be evaluated as either True or False.

Python uses True and False values to "decide" if a statement should be executed.

If a condition is evaluated as True, then Python executes the code following the if statement.

If the test evaluates as False, then Python ignores the code following the if statement.
"""
reactions = ['hooray', 'great', 'oh no', 'omg', 'please stop']
for reaction in reactions:
    if reaction == 'omg':
        print(reaction.upper())
    else:
        print(reaction)
""" 
remember from boolean values:

    == equals (remember, must use double ==, since single = is a variable assignment)
    > greater than
    < less than
    != not equal to
    >= greater or equal to
    <= less than or equal to ordered by priority: 

    not - "flips" the operand; requires use of ( ) if not is after operator, e.g. False == (not True), not can be used with common Python objects, such as numbers, strings, lists, etc.
    and - requires both terms to be returned
    or - either terms (or both) will be returned
"""
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")  ## if/else
"""
if conditional test, then do something

else allows you to define another action to be executed if conditional statement fails

reminder: indenting is REALLY important
"""
age = 14
if age >= 16:
    print("You are old enough to drink beer!")
    print("What's in your cup?")
else:
    print("Sorry, you are not old enough to drink beer.")
    print("That better be apple juice in your cup!")

birthday = input("is it your birthday today? (yes/no) ")
if birthday == 'yes':
    print("CONGRATULATIONS!")
else:
    print("I'm sorry :(")

# another version:
if input("is it your birthday today? (yes/no) ") == "yes":
    print("congratulations!")
else:
    print("I'm sorry :(")  ## pass

# pass means nothing happens

likesPizza = "yes"
pizzaTopping = "mushroom"

if likesPizza == "no":
    pass
else:
    print(f"Preparing your favorite {pizzaTopping} pizza!")  ## if/elif/else chain
"""
The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass. 
As soon as Python finds one test that passes, it skips the rest of the tests. This behavior is beneficial, 
because it’s efficient and allows you to test for one specific condition.# if-elif-else chain

"""
# a pizza with 4 or fewer toppings costs DKK 89.
# a pizza with 5-6 toppings costs DKK 109.
# a pizza with 7 or more toppings costs DKK 129.

howManyToppings = 8

if howManyToppings <= 4:  # if there are 4 or fewer toppings
    print("Your pizza costs DKK 89.")  # print message
elif howManyToppings <= 6:  # if there are 6 or fewer toppings (remember: we already processed 4 in the previous statement,
    # so our options here are only 5 or 6)
    print("Your pizza costs is DKK 109.")  # print message
else:  # if our number of toppings is not between 0 and 6
    print("Your pizza costs DKK 129.")  # print message

howManyToppings = 8
if howManyToppings <= 4:
    price = 89
elif howManyToppings <= 6:
    price = 109
else:
    price = 129

print(f"Your pizza costs DKK {price}.")

# checking for special items in list:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:  # for every topping in list of requested toppings
    if requested_topping == 'green peppers':  # check if the topping is green peppers, if yes
        print("Sorry, out of green peppers!")  # print message
    else:  # if topping is not green peppers, then
        print(f"Adding {requested_topping}.")  # print message

print("\nFinished making your pizza!")

# checking that a list is not empty:
# create empty list
requested_toppings = []

if requested_toppings:  # if there is anything in requested toppings list
    for requested_topping in requested_toppings:  # then for each individual topping from list
        print(f"Adding {requested_topping}.")  # print a message
    print(
        "\nFinished making your pizza!")  # after messages for all individual toppings are printed, print another message
else:  # otherwise (if there is nothing in requested topping list)
    print("Are you sure you want a plain pizza?")  # print a message

# using multiple lists:
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:  # for every topping in requested toppings list
    if requested_topping in available_toppings:  # if requested topping is in available toppings list
        print(f"Adding {requested_topping}.")  # then add it to pizza / print message
    else:  # if requested topping is NOT in the available toppings list
        print(f"Sorry, we don't have {requested_topping}.")  # then apologize / print message

print("\nFinished making your pizza!")  ## break

"""
break stops execution of a loop

note: you cannot break out of an if statement, only out of a loop
"""
requested_toppings = ['mushrooms', 'olives', 'extra cheese']
allergies = ['olives']

for requested_topping in requested_toppings:
    if requested_topping in allergies:
        print(f"Sorry, we cannot complete your order because you are allergic to {requested_topping}.")
        break
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished preparing your order!")

"""
Error handling and the try -- except -- else -- finally conditional

When attempting a command that may fail, the try -- except -- else -- finally key words allows us to give 
alternatives in the case the command we are trying gives an error. 
It is important that you know what kind of error you expect so that you can act accordingly. 
For example, a type conversion may not work with certain input generating a ValueError or NameError when calling
variable that does not exist, or TypeError when doing math operations with incompatible types.  In general all function 
calls can result in different errors, so you should be aware of what types of errors you would be expecting. 

There are two kinds of errors: syntax, and exceptions

## syntax errors
the most common kind: typos, wrong indentation, etc.
information about the error is included in the error message, and are generally highlighted in red in PyCharm
"""
# uncomment the next two line to see a syntax error.
# while True
#     print('Ok')

"""    
## exceptions
even if a statement or expression is syntactically correct, it may cause an error when we execute it.
Those errors are called exceptions: unwanted events that interrupt the normal flow of the program.
when an exception occurs in the program, we get a system-generated message. 
But in Python, we can provide a meaningful message to the user about the issue rather than relying 
on a system-generated message (which is not always understandable anyway).
"""
# examples of system generated error messages.
10 * (1 / 0)

4 + spam * 3

'2' + 2

"""
## exception handling using try -- except -- finally

Handling of exception ensures that the flow of the program does not get interrupted when
an exception occurs which is done by trapping run-time errors. Handling of exceptions
results in the execution of all the statements in the program.

# in simpler terms: the syntax goes something like this
#
# try:
#     do something
# except:
#     do something else when an error occurs
"""
try:
    answer = 12 / 0
    print(answer)
except:
    print("an error occurred")


try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number: "))
    answer = userInput1 / userInput2
    print(f"The answer is {answer}.")
except ValueError:
    print("Error: You did not enter a number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


try:
    userInput = int(input("Please choose a number between 0 and 15: "))
    print(f"You entered {userInput}.")
except ValueError:
    print("That was not a number!")
else:
    print("That will be the number of cookies you get for dinner.")
finally:  # finally is always executed regardless of the actions done about the error
    print("Don't forget to brush your teeth.")
"""
## define something to be an error! the raise key word
"""
name = "Suzie"
if len(name) < 10:
    raise ValueError(f"username {name} too short, must be minimum 10 characters.")

"""
## example: doing math on user input
I am writing code that will take user's input, and multiply it by 2
"""
# simplest option
userInput = float(input("Give me a number to multiply by 2: "))
print(f"{userInput} * 2 = {userInput * 2}")
# but what if I want the user to keep giving me numbers until they say
# "stop"?

active = True  # flag
while active:
    userInput = input("Give me a number to multiply by 2: ")
    if userInput == "stop":
        active = False
    else:
        print(f"{userInput} * 2 = {float(userInput) * 2}")

# here my only input choices are numbers or "stop",
# otherwise code crashes

while True:
    userInput = input("Give me a number to multiply by 2: ")
    if userInput == "stop":
        break # leave while loop
    elif not userInput.isdigit(): # the input is not a string that can be made into a number
        print("sorry, I can only multiply numbers")
    else: # we are ok to multiply
        print(f"{userInput} * 2 = {float(userInput) * 2}")
print("thanks for doing math with me!")

# The same result using try and not having to check all possibilities
while True:
    userInput = input("Give me a number to multiply by 2: ")
    if userInput == "stop":
        break
    try:
        num = float(userInput)  # assume here that conversion of text to number will work
    except:
        print("Not a number!")  # when conversion fails
    else:
        print(float(userInput) * 2)
print("thanks for doing math with me!")

# if the float() function fails because of a letter instead of a number.
while True:
    input1 = input("Type a number as the numerator: ")
    input2 = input("Type a number as the denominator: ")
    if input1.strip() == "stop" or input2.strip() == "stop":
        break
    try: # try this command
        numb1 = float(input1)
        numb2 = float(input2)
        result = numb1/numb2
    except ValueError: # only run if this specific error is thrown by the function in try
        print("One of the numbers is not valid !")
    except ZeroDivisionError:
        print("The denominator cannot be 0!")
    else: # if there are no errors we thrown
        print("{}/{}={}".format(numb1, numb2, result))
    finally: # do this allways no matter which block (except or else) has been used.
        print("That was fun!")
print("Thanks for calculating divisions with me. Bye!")

# There can be several different except block, but only one else and finally blocks.
# Several errors can also be combined into one except block. The draw-back is that all
# errors are treated in the same way.
while True:
    input1 = input("Type a number as the numerator: ")
    input2 = input("Type a number as the denominator: ")
    if input1.strip() == "stop" or input2.strip() == "stop":
        break
    try: # try this command
        numb1 = float(input1)
        numb2 = float(input2)
        result = numb1/numb2
    except (ZeroDivisionError, ValueError):
        print("One of the numbers is not valid or the denominator is 0! ")
    else: # if there are no errors we thrown
        print("{}/{}={}".format(numb1, numb2, result))
    finally: # do this allways no matter which block (except or else) has been used.
        print("That was fun!")
print("Thanks for calculating divisions with me. Bye!")