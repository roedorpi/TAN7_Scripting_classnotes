"""
NESTING
nesting is essentially making a list of dictionaries, a list of items as values in a dictionary or
as a dictionaries as values in a dictionary.  There are many possible combinations that can serve
different purposes. Beware of deeply nested structures, this generally means that an easier solution exists.

"""
# a list of dictionaries

# each fruit is it's own dictionary
fruit_1 = {'type': 'apple', 'color': 'red', 'size': 'medium', 'taste': 'sweet'}
fruit_2 = {'type': 'banana', 'color': 'yellow', 'size': 'medium', 'taste': 'sweet'}
fruit_3 = {'type': 'pear', 'color': 'green', 'size': 'medium', 'taste': 'sweet'}

# list of dictionaries / list of fruit
fruit = [fruit_1, fruit_2, fruit_3]

for eachOne in fruit:
    print(eachOne)


# make a basket of 15 identical fruit (apples)

# Make an empty list for storing apples
fruit = []
# Make 15 red apples. If by any chance you used the fruit_1 variable and do not create a new
# instance at each cycle of the loop python will create links to the original variable, so
# if you change one element of the fruit list you will change all, and we do not want that.
for apple_number in range(15):
    fruit.append({'type': 'apple', 'color': 'red', 'size': 'medium', 'taste': 'sweet'})
    
# Show the first 5 apples
for apple in fruit[:5]:
    print(apple)
print("...")

#Show how many apples you created
print(f"Total number of apples in the basket: {len(fruit)}")

# modify first 3 fruit to be green pears and the next 5 to blue bananas
count = 0
for eachOne in fruit[:8]:
    if eachOne['type'] == 'apple' and count < 3:
        eachOne['type'] = 'pear'
        eachOne['color'] = 'green'
    else:
        eachOne['type'] = 'banana'
        eachOne['color'] = 'blue'
    count += 1
        
# show the first 8 fruit
for eachOne in fruit[:8]:
    print(eachOne)


"""
## a list in a dictionary

In the following example, two kinds of information are stored for each
pizza: a type of crust and a list of toppings. The list of toppings is a value
associated with the key 'toppings'. To use the items in the list, we give the
name of the dictionary and the key 'toppings', as we would any value in the
dictionary. Instead of returning a single value, we get a list of toppings:

"""
# Store information about a pizza being ordered.
pizza = {
    'size': 'small',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['size']}-size pizza ""with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
    
# You can nest a list inside a dictionary any time you want more than
# one value to be associated with a single key in a dictionary.

spoken_languages = {
    'anna': ['polish', 'english', 'danish'],
    'sasha': ['russian', 'german'],
    'jin': ['korean', 'english'],
    'jonathan': ['french', 'english'],
    'phil': ['english'],
    }

for name, languages in spoken_languages.items():
    print(f"\n{name.title()} can speak the following languages:")
    for language in languages:
        print(f"\t{language.title()}")
        
# You should not nest lists and dictionaries too deeply. If you’re nesting items much
# deeper than what you see in the preceding examples or you’re working with someone
# else’s code with significant levels of nesting, most likely a simpler way to solve the
# problem exists.

"""
## a dictionary in a dictionary

For example, if you have several users
for a website, each with a unique username, you can use the usernames as
the keys in a dictionary. You can then store information about each user by
using a dictionary as the value associated with their username. In the following
listing, we store three pieces of information about each user: their
first name, last name, and location.
"""
users = {
    'msco': {
        'first': 'michael',
        'last': 'scott',
        'position': 'regional manager',
        },
    'dshr': {
        'first': 'dwight',
        'last': 'shrute',
        'position': 'assistant to the regional manager',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    position = user_info['position']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tJob title: {position.title()}")

