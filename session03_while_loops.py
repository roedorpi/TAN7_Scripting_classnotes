"""
# # WHILE LOOPS
# definition: a while-loop keeps running as long as (or: while) a certain condition is true
# (for comparison, a for-loop executes a block of code once FOR each item in a list etc.)

# example: using a while loop to count down from 1 to 5
"""
current_number = 1 # current number counter: starts at 1
while current_number <= 5: # while current numbers is less or equal than five
    print(current_number) # print that number
    current_number += 1 # increase current number counter by 1


# example with input function: let the user decide when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message.strip() != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


""" 
## using a flag
in more complicated programs, there's usually more than one event that could stop the program from running
think about computer games: there are many ways to end the game, such as running out of time, running out 
of items, etc. Trying to test all those conditions with individual while statements becomes complicated and 
messy. For a program that should run as long as many conditions are true, we define a single variable that 
determines whether or not the program is active. This variable is called a flag. 

A flag set to true means program runs. A flag set to false means program stops. 
"""

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True # this is our flag!

while active: 
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)


"""
## using break to exit a loop
to exit a while loop immediately and without running any remaining code regardless of anything, 
use the break statement 

"""
# here there is no flag, the break is inserted when the stop condition is reached
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

"""
## using continue in a loop
return to the beginning of the loop based on the result of a conditional test 
"""
# count from 1 to 10, but only print odd numbers:
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: # modulo: if zero, then number is divisible by 2
        continue # continue, or ignore rest of loop, and return to beginning
    print(current_number)

"""
## infinite loops
"""
# this code will run until you terminate it!
x = 1
while x <= 5:
    print(x)

"""
## using a while loop with lists and dictionaries

moving items from one list to another

example: you have a list of homework for courses you need to finish. 
After you finish, you move them to a separate list of finished homework. 
"""
# Start with homework that is not yet finished,
# and an empty list to hold finished homework.
unfinished_homework = ['scripting', 'dig_anthro', 'framing_transf', 'semester project']
finished_homework = []

# finish each homework until there is no more unfinished homework. 
# Move each finished homework into the list of finished homework.
while unfinished_homework:
    current_homework = unfinished_homework.pop()
    print(f"Doing homework: {current_homework}")
    finished_homework.append(current_homework)
    
# Display all confirmed users.
print("\nThe following homework is finished:")
for finished_course in finished_homework:
    print(finished_course)



# removing all instances of specific values from a list
# (cats don't get along with other pets)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    print(pets)


# filling a dictionary with user input:
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("What is your favorite snack? ")
    # Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.abs
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()}'s favorite snack is {response}.")

