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