"""
Session 01 exercise solutions
Exercise 1
Make a program that takes a string and an integer as input from the user
and returns a new string containing the letters from the original string
shifted in the alphabet by the given amount.
For example, “cheer” shifted by 7 is “jolly” and “melon” rotated by −10
is “cubed”.
"""
# this is an external library that gives the functionality to terminate the program
import sys
# Make strings that contain all the letters of the alphabet in the correct order.
# here I have the option of english or danish
letters_DK = 'abcdefghijklmnopqrstuvxyzåæø'
#letters_UK = 'abcdefghijklmnopqrstuvwxyz'
letters_UK = 'abcde'
# get data inputs from the console:
language = input('English (UK) or Danish (DK)? ')
input_string = input('Write a word... any word: ').strip()
output_string = ''
# convert the string input into an integer to use it as a number
shift = int(input('Number of letters to shift by: '))

# choose which alphabet to use
if language.upper() == 'DK':
    letters_ = letters_DK
elif language.upper() == 'UK':
    letters_ = letters_UK
else:
    letters_ = ''
    print('Language should be DK or UK... start again!')
    sys.exit(0) # stop program execution and exit the program
letters_length = len(letters_)
# go through the input string one letter at the time, find the corresponding
# index for that letter in the alphabet, add the shift.
for a in input_string:
    index_of_a = letters_.index(a)
    new_index = index_of_a + shift
    # check if we need to wrap around to the beginning of the alphabet
    if new_index >= letters_length:
        # using de remainder after division we can find the new index
        # no matter how many times we have to wrap around to the beginning
        # of the alphabet.
        new_index = new_index % letters_length

    # add the new letter to the output string.
    output_string += letters_[new_index]
# print the output using an f-string and the variables used in the program.
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
