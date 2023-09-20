"""
BOOlEAN VALUES
definition: booleans represent one of two values: True or False

== equals (remember, must use double ==, since single = is a variable assignment)
> greater than
< less than
!= not equal to
>= greater or equal to
<= less than or equal to
These operators can be used to compare values try it:
"""
1 == 1
"potato" > "potato"


"""
boolean operators are ordered by priority: 

not -   "flips" the operand; requires use of ( ) if not is after operator, e.g. False == (not True), 
        not can be used with common Python objects, such as numbers, strings, lists, etc.
and -   requires both terms to be returned
or -    either terms (or both) will be returned

Predict the outcome or each line
"""
True and True
True and False
False and False
False and True

True or True
True or False
False or False
False or True

not True
not False

"""
Control Structures

The if statement is used to control the flow of a program in its simples form it looks like:   

"""
a, b, c = 0.5, 0.3, 0.7
outcome = 0
# increment outcome if condition is true, do nothing otherwise
if a > b:
    outcome += 1

print(outcome)

# decrease counter if condition is not true
outcome = 0
if a > b:
    outcome += 1
else:
    outcome -= 1

print(outcome)

# check another condition
outcome = 0
if a > b:
    outcome += 1
elif a > c:
    outcome += 1
else:
    outcome -= 1

print(outcome)

# Check two conditions at once:
outcome = 0
if a > b and a > c:
    outcome += 2
elif a > b or a > c:
    outcome += 1
else:
    outcome -= 1
print(outcome)

""" 
For Loops... just the beginning. 
The for loop has the key words "for", "in", and the ending ":"
all statements in the tab group will be executed repeatedly until all the elements a collection of values.       
"""
my_string = "now things are starting to get serious"
a = my_string[3]
print(a)
# Going through the elements of a string.
for a in my_string:
    print(a)
# here we use the function range(), that gives a set of values to iterate over. in this case from 0 to
# the number of characters in the string minus 1 (why the minus one?).
for i in range(len(my_string)-1):
    print(my_string[i])