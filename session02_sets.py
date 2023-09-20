"""
SETS
definition: a collection of unique items without a particular order (position does not matter in sets),
so we can't rely on indexing (no [] or [:]) every set element is unique (no duplicates)

different ways to create sets:
"""
s1 = set()
s3 = {1, 2, 3} # three integers
s4 = {1, "two", 3.0} # mixing is allowed
s5 = {1, 1, 1} # three identical integers, try printing it and see what happens

type(s1)
"""
you can also use the len() function with sets

make a set out of a list:
"""
primes20list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
primes20set = set(primes20list)
len(primes20set)
"""
add items to set
.add()
"""
myset = set()
myset.add(1)
print(myset)

"""
Remove items from set
.discard() leaves the set unchanged if the element is not present in the set

.remove() will raise an error if element is not present in the set

if you use .pop() then a random item will be removed, since sets are unordered

.clear() will also remove all the items from a set
"""
s1 = {1, 2, 3, 4, 5, 6}
s1.discard(4)
print(s1)

s1.discard(7)
print(s1)

s1.remove(1)
print(s1)

s1.remove(7)
print(s1)
"""
set operations
set union: | a set of all elements from both sets; it can also be accomplished using .union() method
"""

A = {1, 2, 3}
B = {4, 5, 6}
print(A | B)
print(A.union(B))
"""
set intersection: & a set of elements that are common in both sets; it can also be accomplished 
using the .intersection() method
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A & B)
print(A.intersection(B))
"""
set difference: - a set of elements that are only in A but not in B; it can also be accomplished 
using the .difference() method
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B)
print(A.difference(B))

"""
set symmetric difference: ^ a set of elements in A and B but not in both; it can also be accomplished 
using the .symmetric_difference() method
"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A ^ B)
print(A.symmetric_difference(B))

odd = {1,3,5,7,9,11,13,15,17,19,21,23,25}
squares = {1,4,9,16,25}
powers = {1,2,4,8,16}

# Which of the squares ARE ALSO an odd number?
print(odd&squares)

# Which of the powers are square?
print(squares&powers)

# What numbers from 1 to 25 are "missing" in odd, squares, and powers together?
allnumbers = set(range(1, 26))  # All numbers from beginning to end, but leaves off the last one.
all_odd_sqr_power = odd | squares | powers
print(allnumbers - all_odd_sqr_power)

"""
set membership test
we can test if item exists in a set or not
"""
A = {1, 2, 3, 4, 5}
7 in A


"""
Manipulating sets
"""
# define what you have in the kitchen
inFridge = {'milk', 'butter', 'sour cream', 'eggs', 'orange juice', 'cola', 'ketchup', 'mayo'}
inFreezer = {'ice cream', 'ice', 'pizza'}
inCabinet = {'tomato sauce', 'garlic', 'basil', 'pepper', 'salt', 'rice', 'beans', 'nutella'}
inBar = {'gin', 'rum'}

# define what you need to cook the menu
starter = {'nacho chips', 'cheddar', 'salsa', 'avocado', 'sour cream'}
main = {'buns', 'burgers', 'tomato', 'lettuce', 'pickles', 'onions', 'ketchup', 'mayo', 'fries'}
dessert = {'ice cream', 'milk', 'whipped cream', 'strawberries'}
drinks = {'vodka', 'orange juice', 'cola', 'beer', 'ice'}

# turns out, the milk went sour in the fridge
# hint: remove milk from the fridge
inFridge.remove('milk')   # this only works if the item exists
inFridge.discard('milk')  # if the item does not exist it does nothing

# make a shopping list
allAtHome = inFridge | inFreezer | inCabinet | inBar
allNeeded = starter | main | dessert | drinks
shoppingList = allNeeded - allAtHome

# your guests want to drink gin and tonics (gin, tonic, ice, and limes) at dinner; what should they bring?
# hint: they need to bring ingredients that are required for gin and tonic
# hint: there is no need to bring ingredients that are in your kitchen and on your shopping list
ginTonic = {'gin', 'tonic', 'ice', 'limes'}
bringGinTonic = ginTonic - allAtHome - allNeeded

# one of your guests requested you add mustard to your shopping list
shoppingList.add('mustard')

# one of your guests is allergic to peanuts; confirm that the food at dinner is safe for them
# hint: check if there are peanuts in the dinner menu
allergy = {'peanuts'}
allergy in allNeeded

# the dinner party is on a Friday evening. Assume that if an ingredient is in the dinner party menu,
# it will all be eaten. You go into your kitchen on Saturday morning. What food do you have in the kitchen then?
leftoverFood = allAtHome - allNeeded

# your roommate wants to know which ingredients from the kitchen you used to cook dinner
usedToCook = allAtHome & allNeeded
