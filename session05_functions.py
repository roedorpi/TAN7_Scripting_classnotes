#!/usr/bin/env python
# coding: utf-8


def welcome():
    """Display a simple welcome message."""
    print("Welcome to TAN7!")


welcome()


# %%

def welcome_student(studentname):
    """Display a simple welcome message."""
    print(f"Hello, {studentname.title()}!")


welcome_student('rodrigo')
welcome_student()  # error - username was missing


# %%

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet('harry', 'hamster')


# %%
# ## keyword arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# %%
# ## default values

def describe_pet(pet_name, animal_type='dog'):  # order matters: defaults are last
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')
describe_pet('wonka')


# %%
# ## equivalent function calls

def describe_pet(pet_name, animal_type='dog'):  # order matters: defaults are last
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# a dog named willie:
describe_pet(pet_name='willie')
describe_pet('willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# %%
# ## return values

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# %%
# ## making an argument optional


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# %%
# ## returning a dictionary


def build_person(first_name, last_name, age=None):  # none is a placeholder value,
    # for when a variable has no specific value assigned to it
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# %%
# ## using a function with a while loop!


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)  # I use my function here
    print(f"\nHello, {formatted_name}!")


# %%
# ## passing a list


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['aleksandra', 'fluffy', 'max']
greet_users(usernames)

# %%
# ## modifying a list in a function


# Start with some cats that need to be hugged.
cats_to_be_hugged = ['fluffy', 'whiskers', 'salem']
hugged_cats = []

# Simulate hugging each cat, until none are left unhugged.
# Move each cat name to hugged_cats after hugging.
while cats_to_be_hugged:
    current_cat = cats_to_be_hugged.pop()
    print(f"Hugging cat: {current_cat.title()}")
    hugged_cats.append(current_cat)

# Display all hugged cats.
print("\nThe following cats have been hugged:")
for cat in hugged_cats:
    print(cat.title())


# %%

def hug_cats(cats_to_be_hugged, hugged_cats):
    """
    Simulate hugging each cat, until none are left unhugged.
    Move each cat to hugged_cats after hugging.
    """
    while cats_to_be_hugged:
        current_cat = cats_to_be_hugged.pop()
        print(f"Hugging cat: {current_cat.title()}")
        hugged_cats.append(current_cat)


def show_hugged_cats(hugged_cats):
    """Show all the cats that were hugged."""
    print("\nThe following cats have been hugged:")
    for cat in hugged_cats:
        print(cat.title())


cats_to_be_hugged = ['fluffy', 'whiskers', 'salem']
hugged_cats = []

hug_cats(cats_to_be_hugged, hugged_cats)
show_hugged_cats(hugged_cats)


# %%


# same code as above, but different variable names:
def hug_cats(before_hug, after_hug):
    """
    Simulate hugging each cat, until none are left unhugged.
    Move each cat to hugged_cats after hugging.
    """
    while before_hug:
        current_cat = before_hug.pop()
        print(f"Hugging cat: {current_cat.title()}")
        after_hug.append(current_cat)


def show_hugged_cats(hugged_list):
    """Show all the cats that were hugged."""
    print("\nThe following cats have been hugged:")
    for cat in hugged_list:
        print(cat.title())


cats_to_be_hugged = ['fluffy', 'whiskers', 'salem']
hugged_cats = []

hug_cats(cats_to_be_hugged, hugged_cats)
show_hugged_cats(hugged_cats)  # %%


def make_pizza(*toppings):  # *args
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza('pepperoni')
make_pizza('pepperoni', 'mushrooms', 'olives')


# %%

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('pepperoni', 'mushrooms', 'olives')


# %%
# ## mixing positional and arbitrary arguments


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'pepperoni', 'mushrooms', 'olives')


# %%
# ## using arbitrary keyword arguments


def build_profile(first, last, **user_info):  # **kwargs
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# # STYLING FUNCTIONS

# some things to keep in mind:
# - functions should have descriptive names, and those names should use lowercase letters and underscores
# - every function should have a comment that explains concisely what it does
# - that comment should appear immediately after the function definition and use the docstring (""") format
# - if you specify a default value for a parameter, no spaces should be used on either side of the equal sign; same goes for keyword arguments
# - it is generally recommended that you limit lines of code to 79 characters so every line is visible in a reasonably sized window; If a set of parameters causes a function’s definition to be longer than 79 characters, press enter after the opening parenthesis on the definition line. On the next line, press tab twice to separate the list of arguments from the body of the function, which will only be indented one level.
# - if your program or module has more than one function, separate them by two blank lines so it is easier to see where one function ends and the next one begins
# - all import statements should be written at the beginning of the file (the only exception is if you have comments explaining code)
