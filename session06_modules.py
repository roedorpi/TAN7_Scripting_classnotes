#!/usr/bin/env python
# coding: utf-8
"""
 STORING FUNCTIONS AS MODULES

 https://docs.python.org/3/tutorial/modules.html

 A module is a file ending in .py that contains the code you want to import into your program.

 download pizza.py from moodle. The file contains one function, make_pizza:

"""

import pizza # this line tells Python to import the pizza.py file, and copy all the functions
            # from there into this program

pizza.make_pizza(16, 'pepperoni') # to call a function from an imported module, enter
                                # the module name, followed by a dot, 
                                # followed by the name of the function
pizza.make_pizza(12, 'pepperoni', 'mushrooms', 'olives')


# importing specific functions:
from pizza import make_pizza # you can put multiple here, separate by ,

make_pizza(16, 'pepperoni') # we imported the function directly, so no need for 'pizza.'
make_pizza(12, 'pepperoni', 'mushrooms', 'olives')

"""
## using 'as' to give a function an alias
useful if the name of a function you're importing might conflict with other names in your program, or the function name is long
"""

from pizza import make_pizza as mp
mp(16, 'pepperoni') 
mp(12, 'pepperoni', 'mushrooms', 'olives')

"""
## using 'as' to give a module an alias
"""

import pizza as p

p.make_pizza(16, 'pepperoni') # to call a function from an imported module, enter
                                # the module name, followed by a dot, 
                                # followed by the name of the function
p.make_pizza(12, 'pepperoni', 'mushrooms', 'olives')

"""
## import all functions in a module
"""

from pizza import *

make_pizza(16, 'pepperoni') 
make_pizza(12, 'pepperoni', 'mushrooms', 'olives')


# # finding out what functions are in a module

dir(pizza)

help(make_pizza)

import math

dir(math)

help(math.sqrt)



from collections import defaultdict
help(defaultdict)


