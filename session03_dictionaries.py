"""
DICTIONARIES

Definition: a dictionary in Python is a collection of key-value pairs.
Each key is connected to a value, and you can use a key to access the
value associated with that key.  A key's value can be a number, a string,
a list, or even a different dictionary: any object you can create in
Python can also be a value in a dictionary. But a key can only be a number
or a string.

You can have an unlimited number of key-value pairs in a dictionary

Starting with an empty dictionary: variableName = {}
"""
# creating a dictionary using the function
pineapple = dict()
pineapple['key'] = 'value'
pineapple['key2'] = 'value2'
print(pineapple)
# using {} and : to separate each key and value, key and value here correspond to actual inputs
pineapple = {'key': 'value', 'key2': 'value2'}
print(pineapple)
# if you use just {} without : you will end up with a set, not a dictionary
pineapple_not_a_dict = {'key', 'value', 'key2', 'value2'}
print(pineapple_not_a_dict)

# a silly dictionary showing the mapping of keys to values:

numbers = dict()
numbers[1] = "one"
numbers[2] = "two"
numbers[3] = "three"
print(numbers)

numbers[20] = "twenty"
numbers[21] = numbers[20]+ " " +numbers[1]
print(numbers)

alsoNumbers = dict()
alsoNumbers['one'] = 1
alsoNumbers['two'] = 2
alsoNumbers['three'] = 3
print(alsoNumbers)

# a simple dictionary:
pineapple = {'Danish': 'ananas', 'color': 'yellow'}
print(f"A pineapple in Danish is called {pineapple['Danish']} and is also {pineapple['color']}!")

# add more features:
pineapple['taste'] = 'acidic'
pineapple['price'] = 16
print(pineapple)
# values are mutable
print(f"Pineapples are {pineapple['color']}.")

pineapple['color'] = 'green'
print(f"Pineapples are now {pineapple['color']}.")

# keys are immutable.
# Example script for adding you own item to the dictionary
lastnames = dict()  # define an empty dictionary
# add key:value pairs
lastnames["Chandler"] = "Bing"
lastnames["Rachel"] = "Green"
lastnames["Monica"] = "Geller"

firstname = input("type in name: ").capitalize()

if firstname in lastnames:
    print(f"{lastnames[firstname]} is in the directory")

else:
    print("we don't know anyone by the name of", firstname)

    addperson = input("would you like to add people to the directory? (y/n):").strip()
    while addperson == 'y':
        newname = input("first and last name: ").split()
        lastnames[newname[0].capitalize()] = newname[1].capitalize()
        print(newname[0].capitalize(), newname[1].capitalize(), "was successfully added to dictionary\n")
        addperson = input("Continue adding people? (y/n)").strip()

print("thank you!")
print(lastnames)

# determine how many people can eat one pineapple for dinner based on it's size
pineapple = {'Danish': 'ananas', 'color': 'yellow', 'taste': 'acidic', 'price': 16, 'size': 'medium'}

if pineapple['size'] == 'small':
    feed = 3
elif pineapple['size'] == 'medium':
    feed = 5
else:  # this must be a large pineapple
    feed = 8

# How many room mates started eating the pineapple already:
pineapple['ate today'] = 2
canFeed = feed - pineapple['ate today']

print(f"The pineapple can feed {canFeed} people for dinner.")
# removing key value pairs permanently
print(pineapple)
del pineapple['taste']
print(pineapple)

# a dictionary of similar objects:
native_languages = {
    'anna': 'polish',
    'sasha': 'russian',
    'jin': 'korean',
    'jonathan': 'english'}


print(f"Anna speaks {native_languages['anna'].title()} at home.")

# trying to access a non existing key will result in a KeyError
print(pineapple['weight'])
# use instead the get() method for dictionaries, if the key is not found
# it returns the second argument.
print(pineapple.get('weight', 'no info about weight!!'))

# looping through dictionaries. Dictionaries have both keys and values, that are probably
# needed in the loop. So we use two variables in the for loop instead on only one.

pineapple = {
    'Danish': 'ananas',
    'color': 'yellow',
    'taste': 'acidic',
    'price': 16,
    'size': 'medium'}

for key, value in pineapple.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# iterate through the native_languages dict.
for name, language in native_languages.items():
    print(f"{name.title()}'s native language is {language.title()}.")

# looping through keys only in a dictionary
for name in native_languages.keys():
    print(name.title())

# looping through values only in a dictionary
for val in native_languages.values():
    print(val.title())

# looping through keys is the default behavior when looping through a dictionary
# therefore this also works:
for name in native_languages:
    print(name.title())

friends = ['jin', 'sasha']

for name in native_languages.keys():
    print(name.title())
    if name in friends:
        language = native_languages[name].title()
        print(f"\t{name.title()}, {language} sounds so beautiful!")

# The keys() method can also be used to search the dictionary keys.
if 'erin' not in native_languages.keys():
    print("Erin, we have no idea which language you speak!")
# you can loop through a dictionary's key in a particular order: sorted() alphabetically
# add an extra entry to the dictionary
native_languages['phil'] = 'english'

for name in sorted(native_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# looping through all values in a dictionary: .values() -
# pulls all values without checking for repeats

print("The following languages have been mentioned:")
for language in native_languages.values():
    print(language.title())

# looping through all values in a dictionary: set() -
# pulls all values WITH checking for repeats
print("The following languages have been mentioned:")
for language in set(native_languages.values()):
    print(language.title())
# careful! building a set by using braces and separating elements with commas:
# It’s easy to mistake sets for dictionaries because they’re both wrapped in braces.
# When you see braces but no key-value pairs, you’re probably looking at a set.

"""
## dictionary comprehension
# why use dictionary comprehension? it's a good substitute for for-loops when building dictionaries 
# but not all for-loops can be written as dictionary comprehension (but all dictionary comprehension can be written 
# as a for-loop :-))
# convert a dictionary of Fahrenheit temperatures into celsius
"""
fahrenheit = {'t1': 90, 't2': 0, 't3': 16, 't4': 32}
celsius = {k: (v-32)*5/9 for (k, v) in fahrenheit.items()}

## adding conditionals to comprehension
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Check for items greater than 2
dict1_cond = {k: v for (k, v) in dict1.items() if v > 2}

# check for items greater than 2 but also need to check if they are multiples of 2 at the same time
dict1_doubleCond = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0}

# check for items greater than 2, and items that are multiples of 2, and items that are multiples of 3
# all at the same time
dict1_tripleCond = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0 if v % 3 == 0}

# if - else conditions

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Identify odd and even entries
dict1_tripleCond2 = {k: ('even' if v % 2 == 0 else 'odd') for (k, v) in dict1.items()}
print(dict1_tripleCond2)

# nested
nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)

"""
DEFAULT DICTIONARIES

Definition: a default dictionary is an empty dictionary, where if a missing key is called on, an empty integer (0) 
or an empty list is assigned automatically (instead of throwing a missing key error)
"""
# defaultdictionaries are not part of the standard Python library so we have to import them
from collections import defaultdict


# 'empty' value of int, which is 0, for new elements
# we are creating a dictionary for which anything that is NOT in it,
# get a value of 0
# so essentially any time we call on a key that does not exist,
# that key gets automatically created, and the assigned value is 0
wow = defaultdict(int)
print(wow['whatever'])

#'empty' value of list, which is an empty list, for new elemwents
# we are creating a dictionary for which anything that is NOT in it,
# the value is an empty list
# so essentially any time we call on a key that does not exist,
# that key gets automatically created, and the assigned value is an empty list
wow = defaultdict(list)
print(wow['whatever'])


# you can define the default string or integer using the lambda argument

wow1 = defaultdict(lambda: "potato")
print(wow1['whatever'])

wow2 = defaultdict(lambda: 42)
print(wow2['whatever'])

# in this example the dictionary is initialized with default int zero.
# in the loop every time is gets a new key argument, creates a new entry.
# if the key exists it add to the value of the entry.

count_words = defaultdict(int)

list_of_strings = ['potato', 'tomato', 'eggplant', 'mushroom', 'onion',
                   'leek', 'garlic', 'squash', 'potato', 'potato',
                   'squash', 'cucumber', 'cucumber']
for veggie in list_of_strings:
    count_words[veggie] += 1
    print(veggie, ":", count_words[veggie])

print(count_words)



