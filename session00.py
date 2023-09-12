# Session 1 Course notes
# Exercises. Familiarize your self with PyCharm and the python console for entering commands.
# Hello world program
print('hello world!')
# Input function that reads keyboard input
name = input('What is your name?')
# use f-string to use a variable as part of a string
status = input(f'so, {name}, how are you doing?')
# the same as before but now with the format method of str objects
name_and_status = "{0} is doing {1}".format(name, status)

# type cast the string input into an integer value
age = int(input(f'{name}, how old are you?'))
# try combining a string and an integer...
name_age_status = name + "is " + str(age) +"year old, and is doing "+ status
# using the format method, integer inputs are converted to stings.
name_age_status = "{0}, is {1} years of old, and is doing {2}".format(name,age,status)

print(name_age_status)

# Make calculations with integers and floats.
a = 5.3
b = 3
print(f'{a} is a float and {b} is an integer')
# float divided by integer
c = a/b
print(f'dividing a float by an integer gives a float, a/b = {c}')

# integer divided by float
c_ = b/a
print(f'the same is true the other way around: b/a = {c_}')

# cast result to integer
d = int(a/b)
print(f"we can cast the results to an integer with the int() function: int(a/b) = {d}")

# remainder after division
e = 7 % 4
print(f'calculating the remainder after division 7 % 4 = {e}')

# hole division, truncated decimal portion
f = 7 // 4
print(f'the hole number division by truncating the decimal portion 7 // 4 = {f}')