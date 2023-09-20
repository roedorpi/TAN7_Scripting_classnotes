"""
LISTS
definition: a list is a collection of items in a particular order (position matters in lists)
you can put anything into a list
"""

vegetables = ['potato', 'carrot', 'beetroot', 'onion']
print(vegetables)

"""
different ways to create lists:
"""

L1 = list()  # this creates an EMPTY list (one with 0 elements)(L1 is a variable of A LIST)
L2 = []  # this is also an EMPTY list
L3 = [1, 2, 3]  # this is a non-empty list with elements separated by commas ,
L4 = [1, "two", 3.1415]  # you can mix types in lists!
L5 = [1, "two", [10, "eleven", 12], []]  # you can put lists in lists too!
"""
finding item in list by position
item order from beginning: 0, 1, 2, 3...

item order from end: -1, -2, -3...

for a four-item list, the positions are:

 0   1   2   3
 A   B   C   D
-4  -3  -2  -1
"""

print(vegetables[0])
print(vegetables[0].title())
print(vegetables[1])
print(vegetables[3])
print(vegetables[-2])

vegetables[2] == vegetables[-2]


"""
L[0] is the first element

len(L) gives you the number of elements

L[-len(L)] is also the first element

L[3:5] is the sublist or slice containing the 4th and 5th element of the list
"""

message = f"Please remember to buy one {vegetables[0]}."
print(message)

otherMessage = f"{vegetables[0].title()} is my favorite vegetable!"
print(otherMessage)

"""
Using an integer variable as index:
"""

a = 2
vegetables[a]


"""
Nested lists 
"""
#         [0    ,      1      ,    2]   -> First list with three elements
#             [0   ,   1    ,  2]       -> Second elements of First list is a three element list
#                 [0 , 1 , 2]           -> Second elements of Second list is also a three element list
#                     [0]               -> Second element of Third list is the last list with one element.
funlist = [1, [2, [3, [4], 5], 6], 7]
print(funlist[1])
print(funlist[1][0]) # print the zero element of element 1
print(funlist[1][1][1][0]) # element 4
funlist[1][1][1] # list containing element 4

"""
A nightmare list, here you have an example of a nested list with elements of different types. 
"""
#              [0, 1,                                   2                                 ]
#                     [   0,                          1                                  ]
#                               [ 0,   1,        2,             3,      4,     5,   6   ]
#                                          [  0,        1  ]
#                                                             [  0  ]
headachelist = [1, 2, ["earth", [3.0, 4.0, ["fire", "water"], ["air"], True, False, [], ]]]

# address the i in fire
headachelist[2][1][2][0][1]

# address the i in air
headachelist[2][1][3][0][1]

"""
Changing, adding, and removing elements

lists are mutable, meaning: we can always change the elements within the list
modifying elements
"""
vegetables[0] = 'peas'
print(vegetables)


"""
Adding elements using .append() - append adds at the end so you can build lists dynamically. 
This is useful if you need to generate data while the program is running. 

"""
vegetables = ['potato', 'carrot', 'beetroot', 'onion']
print(vegetables)

vegetables.append('peas')
print(vegetables)

vegetables = [] # empty list we will fill out
vegetables.append('potato')
vegetables.append('carrot')
vegetables.append('beetroot')
vegetables.append('peas')

print(vegetables)

"""
inserting elements into a specific position in the list

"""
vegetables.insert(1, 'peas')
print(vegetables)

"""
removing elements from the list when you know the exact position of the item using the del keyword.
"""

vegetables = ['potato', 'carrot', 'beetroot', 'onion', 'peas']
print(vegetables)

del vegetables[2]
print(vegetables)
"""
Removing an item using .pop() - takes off the last item from the list and stores it as a new variable
"""
vegetables = ['potato', 'carrot', 'beetroot', 'onion', 'peas']
print(vegetables)

hated_vegetables = vegetables.pop()
print(f"The vegetable I hate the most is {hated_vegetables}.")

"""
Popping item from any position in a list (remember any time you use .pop(), the item is REMOVED from the list)
"""
vegetables = ['potato', 'carrot', 'beetroot', 'onion', 'peas']
print(vegetables)

loved_vegetables = vegetables.pop(0)
print(f"The vegetable I love the most is {loved_vegetables}.")
"""
Removing an item by value
remember that .remove() only removes the first occurrence in a list, so if an item shows up multiple times, 
you'll need a loop
"""

vegetables = ['potato', 'carrot', 'beetroot', 'onion', 'peas']
print(vegetables)

vegetables.remove('carrot')
print(vegetables)

vegetables = ['potato', 'carrot', 'beetroot', 'onion', 'peas']
print(vegetables)

too_orange = 'carrot'
vegetables.remove(too_orange)
print(vegetables)

print(f"\nA {too_orange} is too orange for me.")
print(vegetables)

fruits = ['banana', 'apple', 'orange', 'banana']
print(fruits)
for fruit in fruits:
        if fruit == 'banana':
                fruits.remove('banana')

print(fruits)

"""
Tuples
an immutable list is called a tuple

they are very simple, they behave exactly like lists, except:

you use ( and ) instead of [ and ]
you still use the T[n] and T[a:b] notation to refer to parts
they are immutable, so the T[n] and T[a:b] only works at the right hand side
tuple with one element must include a trailing comma: T = (3,)
"""

vegetables = ('potato', 'carrot', 'beetroot', 'onion')
print(vegetables)

vegetables[1] = 'peas'
print(vegetables)

"""
Organizing lists
sorting permanently with .sort() - alphabetic sorting
"""

fruits = ['banana', 'pineapple', 'apple', 'lemon', 'peach']
print(fruit)
fruits.sort()
print(fruits)

# reverse alphabetical
fruits.sort(reverse=True)
print(fruit)

"""
sorting temporarily with sorted()
"""
fruits = ['banana', 'pineapple', 'apple', 'lemon', 'peach']
print("here's the original list:")
print(fruits)

print("\nHere is the sorted list:")
print(sorted(fruits))

print("\nHere is the original list again:")
print(fruits)

print("\nHere is the reverse-sorted list:")
print(sorted(fruits, reverse=True))
"""
Reverse order of the list permanently using reverse(). This is not a reverse alphabetically as in the example 
with sort(), were only the order of the elements is reversed. 
"""
fruits = ['banana', 'pineapple', 'apple', 'lemon', 'peach']
print(fruits)

fruits.reverse()
print(fruits)
# to go back to the original list use reverse() again.
fruits.reverse()
print(fruits)

"""
find length of a list
"""

len(fruits)
"""
Avoiding index errors when working with lists
"""
fruit = ['banana', 'pineapple', 'apple', 'lemon', 'peach']
print(fruits[5])
"""
Finding position of a specific item
"""
fruit.index('banana')


"""
Indexing in lists a little exercise. Using the following list, write the index notation 
to retrieve the desired output. 
If you are not sure how to start, after initializing the variable try to investigate the list by looking at 
individual elements.
In the console write:
>>> omgWhy[2]
>>> omgWhy[2][3] 
and so on... look at what the interpreter write back and try to get to the correct answer. 

"""

omgWhy = [10, 20, ["Technoanthropology", "coding", ["Python", "PyCharm", "Mars"], [False, False, True, [], [3.14,
        3.3333, ["rubber duck", ["why are you doing this to me?!"], False, ["I like potatoes", "I hate chewing gum",
        "what is this?", ]]]]], 1]

# address the phrase that best describes what you think about this list (output: what is this?)

# address the phrase that best describes what you were thinking while doing the previous exercise
# (output: why are you doing this to me?!)

# address your study program (output: Technoanthropology)

# address the programming language we are learning

# address the software we are using in class

# address the 1

# address the True value

# address the empty list

# address the word 'potatoes' using only 1 line of code

# address the M in Mars

# address the exclamation mark, knowing that it is the last character in a string
