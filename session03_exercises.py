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
##
Recipes = dict()
Recipes["brownies"] = [[1.5, "cup", "sugar"], [0.75, "cup", "flour"],[0.66, "cup", "cocoa powder"],
                           [0.5, "cup", "chocolate chips"], [2, "piece", "egg"], [0.5, "cup", "oil"],
                           [2, "tablespoon", "water"],[0.5, "teaspoon", "vanilla"]]
Recipes["pancakes"] = [[1.5, "cup", "flour"],[3.5, "teaspoon", "baking powder"],[0.25, "teaspoon", "salt"],
                           [1, "cup", "milk"],[1, "tablespoon", "sugar"],[1, "piece", "egg"]]
Recipes["muffins"] = [[2, "cup", "flour"],[3, "teaspoon", "baking powder"],[0.5, "teaspoon", "salt"],
                          [0.75, "cup", "sugar"],[1, "cup", "milk"],[0.25, "cup", "oil"],[1, "piece", "egg"]]
##
""" 
Part a
"""

NumberOfPortions  = 1
Dish = 'brownies'
for dish, ingredients in Recipes.items():
    if dish == Dish:
        print(f"The {dish} dish for {NumberOfPortions} portions needs following ingredientes and quantities:")
        for ingredient in ingredients:
            print(f"\t{ingredient[2]}:{ingredient[0]/4*NumberOfPortions}--{ingredient[1]} ")




##

InKitchen = []
Active = True
while Active:
    NewInKitchen = []
    newigredient = input("write the ingredient, the quantity and the unit of measure? ").split()
    if newigredient[0].strip() == "stop":
        break
    for element in newigredient:
        element.strip()
    try:
        quantity = float(newigredient[1])
    except:
        print("the second input must be a number")
    else:
        NewInKitchen.append(quantity)
        NewInKitchen.append(newigredient[2])
        NewInKitchen.append(newigredient[0])
    InKitchen.append(NewInKitchen)




