"""
Session 01 course notes
Exercise 1
Make a program that takes a string and an integer as input from the user
and returns a new string containing the letters from the original string
shifted in the alphabet by the given amount.
For example, “cheer” shifted by 7 is “jolly” and “melon” rotated by −10
is “cubed”.
"""
# tuples are immutable arrays, that cannot be changed in the program
# they have two useful methods .index() to find the index of a given
# element and .count() to find out how many times a given value occurs

letters_DK = 'abcdefghijklmnopqrstuvwxyzåæø'

letters_UK = 'abcdefghijklmnopqrstuvwxyz'

# get data inputs from the console
language = input('English (UK) or Danish (DK)? ')
input_string = input('Write a word... any word: ')
output_string = ''
# convert the string input into an integer to use it as a number
shift = int(input('Number of letters to shift by: '))

# choose which alphabet to use
if language == 'DK':
    letters_ = letters_DK
elif language == 'UK':
    letters_ = letters_UK
else:
    letters_ = ''
    print('Language should be DK or UK...')

# go through the input string one letter at the time, find the corresponding
# index for that letter in the alphabet, add the shift.
for a in input_string:
    index_of_a = letters_.index(a)
    new_index = index_of_a + shift
    # check if we need to wrap around to the beginning of the alphabet
    if new_index >= len(letters_):
        new_index -= len(letters_)
    # add the new letter to the output string.
    output_string += letters_DK[new_index]
# print the new string.
print(f'The input: {input_string}, shifted by {shift} letters becomes: {output_string}.')


"""
Make a program that changes temperature in degrees Celsius to Fahrenheit, 
using the conversion: C*9/5 + 32 = F

"""

temp_in = int(input('What is the temperature? '))
temp_scale = input('What is the scale of the temperature (Fahrenheit (F) or Celcius (C))? ')

if temp_scale == 'F':
    temp_out = (temp_in - 32)*5/9
elif temp_scale == 'C':
    temp_out = temp_in*9/5 + 32
else:
    temp_out = None
    print('ups')

print(f'The converted temperarure is: {temp_out} degrees {temp_scale}')