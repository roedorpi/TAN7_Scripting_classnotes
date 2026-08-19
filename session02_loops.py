##
"""
FOR LOOPS
definition: a for loop is a definite iteration, which means the same block of code will
be repeated a specified number of times

we are telling python to retrieve the first item in the list kittens, and associate it with the
variable cat; this set of steps is repeated once for each item in the list, no matter how many
items there are: for a million items, there will be a million iterations
"""
kittens = ['whiskers', 'fluffy', 'tiger', 'salem']
for cat in kittens:
    print(cat.title())
##
"""
you can put however many items or commands you want inside the loop
"""
kittens = ['whiskers', 'fluffy', 'tiger', 'salem', 'marla', 'guadalupe', 'garfield']
for cat in kittens:
    print(f"{cat.title()} is the fluffiest cat in the world!")
    print(f"I love {cat.title()} so much.\n")
    if cat=='marla':
        print(f"{cat.title()} is a grumpy cat ")
    if cat=='guadalupe':
        print(f"{cat.title()} cannot stay out of the trash!")

print(f'{cat.title()} damm that cat!')
print(f'{kittens[-1].title()} damm that cat!')

##
"""
Python relies on indentation to determine how a line, or a group of lines, is related 
to the rest of the program to leave a loop, go back an indent

play around with loop indentation
"""
for cat in kittens:
    print(f"{cat.title()} is the fluffiest cat in the world!")
    print(f"I love {cat.title()} so much.\n")

print("Honestly, I just love all cats.")

"""
Use the reversed() function to go through the list backwards
"""
for cat in reversed(kittens):
    print(f"{cat.title()} is the fluffiest cat in the world!")
    print(f"I love {cat.title()} so much.\n")
print("Honestly, I just love all cats, even in another order")

"""
making a numerical list using range()
In this example, range() prints only the numbers 1 through 4. The range() function causes Python to start
counting at the first value you give it, and it stops when it reaches the second value you provide. 
Because it stops at that second value, the output never contains the end value, which would have been 
5 in this case. To print the numbers from 1 to 5, you would use range(1, 6).
"""
##
for value in range(1, 5):
    print(value)
##
"""
if you only give range() a number of items you want to get, without the starting item, it will start at 0:
"""
for value in range(6):
    print(value)
"""
if you give range() three inputs, they are: starting number, how many numbers starting from 0, 
step size when generating numbers:
"""
even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 11, 2))
print(odd_numbers)

"""
You can also use range() with a negative increment to count backwards:
"""
for value in range(10, 0, -1):
    print(value)

"""
using for loops for making lists
make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10):
"""
# 4 lines of code

squares = []  # empty list

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# 3 lines of code: a more concise version
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

"""
optimizing your code: list comprehension

a list comprehension combines the for loop and the creation of new elements into one line, 
and automatically appends each new element.
The brackets create the list, the first argument (before the "for") is the calculation of
new element, note the use of the loop variable "value", that is defined after the "for". 
The final part of the statement tells the loop which elements to use at each iteration. 
"""
# 1 line of code: the most concise version

squares = [value ** 2 for value in range(1, 11)]
print(squares)
"""
Looping through a slice of a list
"""
kittens = ['whiskers', 'fluffy', 'tiger', 'salem', 'tina']
for cat in kittens[2:3]:
    print(cat.title())

"""
make a list out of a set
"""

primes20set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71}
primes20list = []

for prime in primes20set:
    primes20list.append(prime)
print(primes20list)

len(primes20set) == len(primes20list)  # check if all values made it to the list

"""
playing with for loops
"""
primes20set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71}

# what is the sum of the first 20 primes?

theSum = 0  # declaring and initializing
for element in primes20set:  # for all elements in the set primes20
    theSum = theSum + element
print("\n\nThe sum of the first 20 primes is:", theSum)

# what is the sum of the first 10 primes?

anotherSum = 0  # always remember to set this to 0 first
for element in primes20list[0:10]:
    anotherSum = anotherSum + element
print("\n\nThe sum of the first 10 primes is:", anotherSum)

# multiply all members of the set

theMultiplication = 1  # you have to start with 1 bc this is multiplication, not addition
for element in primes20set:
    theMultiplication = theMultiplication * element
print("\n\nThe result of multiplication is:", theMultiplication)

"""
Loops with if statements
"""
# count the number of even numbers that are in this set
# even means number%2==0

how_many = 0
for element in primes20set:
    if element % 2 == 0:
        how_many = how_many + 1
print("\n\nThere are", how_many, "even numbers in this set")

# OR
evens = 0
for element in primes20set:
    if element % 2 == 0:
        evens += 1
print("\n\nThere are", evens, "even numbers in this set")

# with strings
s = "abcdefg"
list_s = []
for character in s:
    list_s.append(character)
print(list_s)

# loop inside a loop:

L2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for element in L2:
    for number in element:
        print(number)


reactions = ['hooray', 'great', 'oh no', 'omg', 'please stop']

for reaction in reactions:
    if reaction == 'omg':
        print(reaction.upper())
    else:
        print(reaction)
"""
More examples of Conditional tests, boolean variables and loops. 

reminder: indenting is REALLY important

"""
# print if one condition is true, do nothing is false
if input("What is the correct answer?") != 42:
    print("That is not the correct answer! Try again.")

# print if one condition is true, print something else if false
if input("is it your birthday today? (yes/no) ") == "yes":
    print("congratulations!")
else:
    print("I'm sorry :(")

"""
pass keyword, means nothing happens
"""
likesPizza = input("Do you like pizza?")
pizzaTopping = input("What is your favorite topping?")
if likesPizza == "no":
    pass # does not like pizza... do nothing
else:
    print(f"Preparing your favorite {pizzaTopping} pizza!")


""" 
if-elif-else chain
Select the correct price for a pizza 
a pizza with 4 or fewer toppings costs DKK 89.
a pizza with 5-6 toppings costs DKK 109.
a pizza with 7 or more toppings costs DKK 129.
"""
howManyToppings = 8

if howManyToppings <= 4:  # if there are 4 or fewer toppings
    print("Your pizza costs DKK 89.")  # print message
elif howManyToppings <= 6:  # if there are 6 or fewer toppings
    # (remember: we already processed 4 in the previous statement,
    # so our options here are only 5 or 6)
    print("Your pizza costs is DKK 109.")  # print message
else:  # if our number of toppings is not between 0 and 6
    print("Your pizza costs DKK 129.")  # print message

"""
Now lets avoid repeating almost identical print staments with a f-string
"""
howManyToppings = 8

if howManyToppings <= 4:
    price = 89
elif howManyToppings <= 6:
    price = 109
else:
    price = 129
print(f"Your pizza costs DKK {price}.")

"""
Checking for special items in list using a for loop
"""
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:  # for every topping li list of requested toppings
    if requested_topping == 'green peppers':  # check if the topping is green peppers, if yes
        print("Sorry, out of green peppers!")  # print message
    else:  # if topping is not green peppers, then
        print(f"Adding {requested_topping}.")  # print message

print("\nFinished making your pizza!")

"""
checking that a list is not empty:
"""
# create empty list
requested_toppings = []

if requested_toppings:  # if there is anything in requested toppings list
    for requested_topping in requested_toppings:  # then for each individual topping from list
        print(f"Adding {requested_topping}.")  # print a message
    print(
        "\nFinished making your pizza!")  # after messages for all individual toppings are printed, print another message
else:  # otherwise (if there is nothing in requested topping list)
    print("Are you sure you want a plain pizza?")  # print a message

"""
Using multiple lists:
"""
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:  # for every topping in requested toppings list
    if requested_topping in available_toppings:  # if requested topping is in available toppings list
        print(f"Adding {requested_topping}.")  # then add it to pizza / print message
    else:  # if requested topping is NOT in the available toppings list
        print(f"Sorry, we don't have {requested_topping}.")  # then apologize / print message

print("\nFinished making your pizza!")

"""
break stops execution of a loop
note: you cannot break out of an if statement, only out of a loop
"""
requested_toppings = ['mushrooms', 'olives', 'extra cheese']
allergies = ['olives']

for requested_topping in requested_toppings:
    if requested_topping in allergies:
        print(f"Sorry, we cannot complete your order because "
              f"you are allergic to {requested_topping}.")
        break
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished preparing your order!")
