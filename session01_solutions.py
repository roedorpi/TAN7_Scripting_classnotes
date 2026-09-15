"""
Session 01 exercise
Exercise 1
Make a program that takes a string and an integer as input from the user and returns a new string containing the letters from the original string shifted in the alphabet by the given amount. For example, “cheer” shifted by 7 is “jolly” and “melon” rotated by −10 is “cubed”.
"""
# this is an external library that gives the functionality to terminate the program
import sys

from session04_nltk_introduction import long_words

# Make strings that contain all the letters of the alphabet in the correct order.
##
word = input('Give me a word:')
shift = int(input('Give me a shift:'))
alphabet = 'abcdefghijklmnopqrtsuvwxyz'
newword = ''
for letter in word:
    if letter in alphabet:
        letter_index = alphabet.find(letter) + shift
        if letter_index > len(alphabet) - 1:
            letter_index = letter_index%len(alphabet)
        newword += alphabet[letter_index]
    else:
        print(f'{letter} not in the alphabet')
print(newword)
##
"""
Exercise 2
Make a program that changes temperature in degrees Celsius to Fahrenheit, using the conversion: C*9/5 + 32 = F. If you are done and need more, make a function. You will have to read up on the keyword "def" to define the function, and learn how to call it from the console or program. 
"""
def temp_converter(temp, Scale):
    if Scale == 'F':
        out_temp = (temp - 32) * 5/9
    else:
        out_temp = temp * 9/5 + 32
    return out_temp

Temp = temp_converter(32,'F')


"""
Exercise 3
Make a program that can find all the repeated words in a sentence, and returs the repeated words and the number of occurrences.

Make a program that can calculate the lexical complexity and the percentage of occurrence for a given word a text. You can use the tools presented in ch.1 of the NLTK book.  

Once the program is running, make it into a function. 
"""
##
Sentence = 'This is a sentence that should not have repeated words but it is unlikely that you can manage this with out using some repeated words at all.'

# lexical complexity: average length of words * ratio between the number of unique words and number of words in the text

sentence = Sentence.split()
numb_of_words = len(sentence)
vocab_length = len(set(sentence))
mean_word_length = 0
for word in set(sentence):
    mean_word_length += len(word)
mean_word_length = int(mean_word_length/vocab_length)

Lex_complex = mean_word_length * (vocab_length/numb_of_words)
print(f'The input text has a lexical complexity of: {Lex_complex}')
##
def lexical_diversity(input_text,target_word):
    if type(input_text) is str:
        input_text = input_text.split()
    numb_of_words = len(input_text)
    vocab_length = len(set(input_text))
    mean_word_length = 0
    for word in set(input_text):
        mean_word_length += len(word)
    mean_word_length = int(mean_word_length / vocab_length)
    lex_div = vocab_length/numb_of_words

    target_word_occurrence = input_text.count(target_word)

    return [lex_div, target_word_occurrence, mean_word_length]

def lexical_complexity(input_text):
    sentences = input_text.split('.')
    words = input_text.split()

    long_words = [w for w in words if len(w) > 6]
    lix = len(words) / len(sentences) + 100*len(long_words)/len(words)
    return lix


def find_repeated_words(input_string):
    if type(input_string) is str:
        input_string = input_string.split()
    repeated_words = []
    while len(input_string) > 1:
        word_source = input_string[0]
        number_of_words = len(input_string)
        input_string = [word for word in input_string if word_source != word]
        word_count = number_of_words - len(input_string)
        if word_count > 1:
            repeated_words.append((word_source, word_count))

    return repeated_words




Text = "We have been exploring language bottom-up, with the help of texts and the Python programming language. However, we're also interested in exploiting our knowledge of language and computation by building useful language technologies. We'll take the opportunity now to step back from the nitty-gritty of code in order to paint a bigger picture of natural language processing. At a purely practical level, we all need help to navigate the universe of information locked up in text on the Web. Search engines have been crucial to the growth and popularity of the Web, but have some shortcomings. It takes skill, knowledge, and some luck, to extract answers to such questions as: What tourist sites can I visit between Philadelphia and Pittsburgh on a limited budget? What do experts say about digital SLR cameras? What predictions about the steel market were made by credible commentators in the past week? Getting a computer to answer them automatically involves a range of language processing tasks, including information extraction, inference, and summarization, and would need to be carried out on a scale and with a level of robustness that is still beyond our current capabilities. On a more philosophical level, a long-standing challenge within artificial intelligence has been to build intelligent machines, and a major part of intelligent behaviour is understanding language. For many years this goal has been seen as too difficult. However, as NLP technologies become more mature, and robust methods for analyzing unrestricted text become more widespread, the prospect of natural language understanding has re-emerged as a plausible goal. In this section we describe some language understanding technologies, to give you a sense of the interesting challenges that are waiting for you."

Text = Text.lower()

Rep_words = find_repeated_words(Text)

Lex_comp = lexical_complexity(Text)

Lex_div = lexical_diversity(Text,'all')