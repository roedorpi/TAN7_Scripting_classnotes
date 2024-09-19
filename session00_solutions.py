# Session 1 Course notes
# Exercises. Familiarize your self with PyCharm and the python console for entering commands.
## Hello world program
print('hello world!')
# Input function that reads keyboard input
name = input('What is your name?')
# use f-string to use a variable as part of a string
status = input(f'so, {name}, how are you doing?')
# the same as before but now with the format method of str objects
name_and_status = "{0} is doing {1}".format(name, status)

## type cast the string input into an integer value
age = int(input(f'{name}, how old are you?'))
# try combining a string and an integer...
name_age_status = name + "is " + str(age) +"year old, and is doing "+ status
# using the format method, integer inputs are converted to stings.
name_age_status = "{0}, is {1} years of old, and is doing {2}".format(name,age,status)

print(name_age_status)

## Make calculations with integers and floats.
a = 5.3
b = 3
# float divided by integer
c = a/b
# integer divided by float
c_ = b/a

# cast result to integer
d = int(b/2)

# remainder after division
e = 7 % 4
# hole division, truncated decimal portion
f = 7 // 4

## Calculate years based on number of days:

numDays = int(input('How many days have passed? '))

daysInYear = 356

numYears = numDays/daysInYear

print(f'There are {numYears} years in {numDays} days')


## BMI calculation
name = input('What is your name? ')
weight_height = input('What is your weight in kilograms and height in meters (separate values with a coma)? ')
WeigtHeight = weight_height.split(',')
Weight = float(WeigtHeight[0])
Height = float(WeigtHeight[1])
BMI = round(Weight/pow(Height,2),2)

print(f'Hello {name}, You have a BMI of {BMI}')

