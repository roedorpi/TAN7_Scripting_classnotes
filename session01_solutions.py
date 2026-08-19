
"""
Session 01 exercise solutions
"""
##
"""
Exercise 1
Make a program that takes a string and an integer as input from the user and returns a new string containing the letters from the original string shifted in the alphabet by the given amount. For example, “cheer” shifted by 7 is “jolly” and “melon” rotated by −10 is “cubed”.
"""
# this is an external library that gives the functionality to terminate the program
import sys
# Make strings that contain all the letters of the alphabet in the correct order.
# here I have the option of english or danish
letters_DK = 'abcdefghijklmnopqrstuvxyzåæø'
letters_UK = 'abcdefghijklmnopqrstuvwxyz'

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
    index_of_a = letters_.index(a) # use the string method index()
    new_index = index_of_a + shift
    # check if we need to wrap around to the beginning of the alphabet
    if index_of_a + shift >= letters_length:
        # using de remainder after division we can find the new index
        # no matter how many times we have to wrap around to the beginning
        # of the alphabet.
        new_index = new_index % letters_length
    else:
        new_index = index_of_a + shift

    # add the new letter to the output string.
    output_string += letters_[new_index]
# print the output using an f-string and the variables used in the program.
print(f'The input: {input_string}, shifted by {shift} letters becomes: {output_string}.')

##
"""
Exercise 2
Make a program that changes temperature in degrees Celsius to Fahrenheit, using the conversion: C*9/5 + 32 = F
"""

temp_in = int(input('What is the temperature? '))
temp_scale = input('What is the scale of the temperature (Fahrenheit (F) or Celcius (C))? ')

if temp_scale == 'F':
    temp_out = (temp_in - 32)*5/9
    scale_out = 'C'
elif temp_scale == 'C':
    temp_out = temp_in*9/5 + 32
    scale_out = 'F'
else:
    temp_out = None
    print('ups')

print(f'The converted temperarure is: {temp_out} degrees {scale_out}')

##
"""
Exercise 2b
The same thing but made as a function that takes a string and an integer as input from the user.
"""
#function definition
def temp_convert(temp_in, temp_scale):
    if temp_scale == 'F':
        temp_out = (temp_in - 32)*5/9
        temp_scale_out = 'C'
    elif temp_scale == 'C':
        temp_out = temp_in*9/5 + 32
        temp_scale_out = 'F'
    else:
        temp_out = None
        temp_scale_out = None
        print('ups')

    print(f'The converted temperature is: {temp_out} degrees {temp_scale_out}')

# program that calls the function
temp_in = int(input('What is the temperature? '))
temp_scale = input('What is the scale of the temperature (Fahrenheit (F) or Celcius (C))? ')
# function call
temp_convert(temp_in, temp_scale)

##
"""
Exercise 3
Make a program that can find all the repeated words in a sentence, and returs the repeated words and the number of occurrences.  Once the program is running, make it into a function. 
"""

input_string = input('Write a long sentence with repeated words: ')
sentence = input_string.split()
# here were are declaring a new empty list, which is a container for any type of element.
repeated_words = []
while len(sentence) > 1:
    word_source = sentence[0]
    number_of_words = len(sentence)
    # make a new sentence with out the repeated words
    sentence = [word for word in sentence if word_source != word]
    # if there are no repeated words the new sentence from the previous line should be one element shorter
    word_count = number_of_words-len(sentence)
    # in order to append two values in for each time a repeated word is found, a tuple is used, and is declared using the round parenthesis
    if word_count > 1:
        repeated_words.append((word_source,word_count))

print(f'Repeated words: {repeated_words}')
##
"""
Exercise 3b same as 3 but as a function
"""
# function definition, notice that the only difference is the UK
# first line.
def find_repeated_words():
    input_string = input('Write a long sentence with repeated words: ')
    sentence = input_string.split()
    repeated_words = []
    while len(sentence) > 1:
        word_source = sentence[0]
        number_of_words = len(sentence)

        sentence = [word for word in sentence if word_source != word]

        word_count = number_of_words - len(sentence)

        if word_count > 1:
            repeated_words.append((word_source, word_count))

    print(f'Repeated words: {repeated_words}')

find_repeated_words()
