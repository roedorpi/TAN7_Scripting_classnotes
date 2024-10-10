"""
Making recipes from a cookbook

##part a
Make a grocery list based on recipes below.

your program will first list available recipes, then ask the user to select a recipe
and how many portions the user wants to cook.
Then the program will list:

    1. how much of each ingredient the user will need to make the specified number of portions
       of a recipe (for example, how much of each ingredient do I need to make two portions of brownies?)
    2. how much of each ingredient the user will need to make one portion of ALL available recipes
       (if I want to bake one of everything, how much of each ingredient will I use, in total?)
    3. how much of each ingredient the user will need to make the specified number of portions of
       ALL available recipes (for example, if I want to invite 5 friends over, and bake 5 portions
       of each recipe for them, how much of each ingredient will I use, in total?)


part b

using the same recipes, ask user to input what they have in the kitchen (and how much), and list:

    1. which recipes they can make one portion of (given what I have in the kitchen, what can I
       bake from the cookbook?)
    2. which recipes they can make a specified portion of (given what I have in the kitchen, if
       I want to bake five portions, what can I bake?)


part c

using the same recipes, allow the user to add new recipes to the cookbook using a while loop, the
new recipes have to maintain the same format as the existing recipes.
"""
"""
recipes

Each recipe is for 1 portion, and 1 portion can feed 4 people - if you want to make enough for just 
one person, then you need 1/4 portion):

brownies: 1 1/2 cups sugar, 3/4 cups flour, 2/3 cup cocoa powder, 1/2 cup sugar, 
          1/2 cup chocolate chips, 3/4 teaspoon salt, 2 eggs, 1/2 cup oil, 
          2 tablespoons water, 1/2 teaspoon vanilla

pancakes: 1 1/2 cup flour, 3 1/2 teaspoons baking powder, 1/4 teaspoon salt, 
          1 tablespoon sugar, 1 egg, 3 tablespoons butter, 1 cup milk

muffins:  2 cups flour, 3 teaspoons baking powder, 1/2 teaspoon salt, 
          3/4 cup sugar, 1 egg, 1 cup milk, 1/4 cup oil
"""


##
ingredients = dict()

# every value of this dict is a list of items,
# each item is in its self a list with
# format: [<amount>, <unit>, <ingredient>]

ingredients["brownies"] = [[1.5, "cup", "sugar"],
                           [0.75, "cup", "flour"],
                           [0.66, "cup", "cocoa powder"],
                           [0.5, "cup", "chocolate chips"],
                           [2, "piece", "egg"],
                           [0.5, "cup", "oil"],
                           [2, "tablespoon", "water"],
                           [0.5, "teaspoon", "vanilla"]]

ingredients["pancakes"] = [[1.5, "cup", "flour"],
                           [3.5, "teaspoon", "baking powder"],
                           [0.25, "teaspoon", "salt"],
                           [1, "cup", "milk"],
                           [1, "tablespoon", "sugar"],
                           [1, "piece", "egg"]]

ingredients["muffins"] = [[2, "cup", "flour"],
                          [3, "teaspoon", "baking powder"],
                          [0.5, "teaspoon", "salt"],
                          [0.75, "cup", "sugar"],
                          [1, "cup", "milk"],
                          [0.25, "cup", "oil"],
                          [1, "piece", "egg"]]

## ## operations:
# list available recipes:

print("These recipes are available:\n")
for availableRecipes in ingredients:
    print(availableRecipes)
print("\n")

## user input: what would you like to bake?

wantedName = input("What would you like to bake? ")

# to bake one portion of wanted recipe:

print("To bake one portion of", wantedName, "you will need:\n")
for eachIngredient in ingredients[wantedName]:
    print(eachIngredient[0], eachIngredient[1] + "s", eachIngredient[2])

## user input: how many would you like to bake?

wantedAmount = float(input("How many portions? "))

# to make X amount you need the following shopping list:

print("To bake", wantedAmount, "portions of", wantedName, "you need:\n")
for neededIngredient in ingredients[wantedName]:
    neededAmount = neededIngredient[0] * wantedAmount
    print(neededAmount, neededIngredient[1] + "s of", neededIngredient[2])

## to make one portion of each recipe in cookbook:
from collections import defaultdict

ultimateAmount = defaultdict(float)
ultimateUnit = dict()

for availableRecipes in ingredients:
    for eachIngredient in ingredients[availableRecipes]:
        ultimateAmount[eachIngredient[2]] += eachIngredient[0]
        ultimateUnit[eachIngredient[2]] = eachIngredient[1]

print("To bake one portion of all available recipes you need to buy:\n")
for eachIngredient in ultimateAmount:
    print(ultimateAmount[eachIngredient], ultimateUnit[eachIngredient] + "s of", eachIngredient)

## # part b code

# how much of each ingredient do you have at home? user input
"""In the following code, what is the skypRedundancy set used for? """
userAmount = dict()
skipRedundancy = set()

for availableRecipes in ingredients:
    for eachIngredient in ingredients[availableRecipes]:
        if eachIngredient[2] in skipRedundancy:
            pass
        else:
            userAmount[eachIngredient[2]] = float(
                input(f"how many {eachIngredient[1]}s of {eachIngredient[2]} do you have? "))
            skipRedundancy.add(eachIngredient[2])
print("You have the following ingredients at home:\n")
print(userAmount)


## do you have enough ingredients in your kitchen to bake one portion of recipe of choice (user input)?

recipeCheck = input("I would like to bake one portion of: ")
missingIngredient = list()

for eachIngredient in ingredients[recipeCheck]:
    if eachIngredient[0] > userAmount[eachIngredient[2]]:
        missingIngredient.append(eachIngredient[2])

if len(missingIngredient) == 0:
    print(f"CONGRATULATIONS! You can bake one portion of {recipeCheck}!")
else:
    print(f"Sorry, you do not have enough of: {missingIngredient}.")

## which recipes could you make one portion of, given the ingredients you have in your kitchen?
from collections import defaultdict
canMake = set()
haveFromRecipe = defaultdict(set)
missingFromRecipe = defaultdict(set)

for availableRecipes, recipeIngredients in ingredients.items():
    for eachIngredient in recipeIngredients:
        if eachIngredient[0] > userAmount[eachIngredient[2]]:
            missingFromRecipe[availableRecipes].add(eachIngredient[2])

cantMake = set(missingFromRecipe.keys())
available = set(ingredients.keys())
canMake = available - cantMake
if missingFromRecipe:
    print("You need the following ingredients to make one portion of:")
    for recipes, missing in missingFromRecipe.items():
        print(f"\t {recipes}:")
        for ing in missing:
            print(f"\t\t {ing}")
if canMake:
    print("You can make one portion of:")
    for recipes in canMake:
        print(f"\t{recipes}")



## if you want to make X portions (user input), which recipes could you make X portions of?
"""Do you get the expected results with this code? how can you fix it?"""
canMakeEnough = set()
howManyWant = int(input("How many guests will you host? "))

for availableRecipes, recipeIngredients in ingredients.items():
    for eachIngredient in recipeIngredients:
        if eachIngredient[0] * howManyWant < userAmount[eachIngredient[2]]:
            canMakeEnough.add(availableRecipes)

if len(canMakeEnough) == 0:
    print(f"you cannot make any recipes if {howManyWant} guests come over.")
else:
    print(f"You have enough ingredients to make {canMakeEnough} for {howManyWant} guests!")

## ## part c code

# user adding recipes to cookbook

newRecipeName = input("what is this recipe for? ")
newRecipe = list()

howManyIngredients = int(input("how many ingredients? "))
newIngredientCount = 0

print("I will ask you to write one ingredient at a time: what it is, then what unit it is measured in, \
then how much of that unit is needed in recipe. For example, 1 cup flour means you first write \
flour, then cup, then 1.")
"""is this the correct way of using a while loop? how many time are you going to iterate?
    Is there a better way of dropping out of the while loop?  
"""
while newIngredientCount < howManyIngredients:
    whatIngredient = input(f"enter ingredient {newIngredientCount + 1}: ")
    whatMeasureIng = input("how is it measured? (options: cup, tablespoon, teaspoon, piece): ")
    howMuchIng = float(input("how much is needed? "))

    newIngredient = list()
    newIngredient.append(howMuchIng)
    newIngredient.append(whatMeasureIng)
    newIngredient.append(whatIngredient)

    newRecipe.append(newIngredient)

    newIngredientCount += 1

ingredients[newRecipeName] = newRecipe

print("The following recipes are available to you: ")
for availableRecipes in ingredients:
    print(availableRecipes)

