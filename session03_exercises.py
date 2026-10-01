##
import os
import string

import nltk
from nltk.corpus import gutenberg, PlaintextCorpusReader
from nltk import FreqDist, ConditionalFreqDist
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")


##
"""
Assignment 01 Session 03
1. Write a program to calculate the frequency distribution of the length of words and the length of sentences of a text.
"""

##
# Using the NLTK Gutemberg corpus, we can analyze the text of "Alice's Adventures in Wonderland" by Lewis Carroll. We can use the built-in tokenizers of the gutemberg corpus to split the text into words and sentences or load the text as it is on the original file with the raw() method.
# the eazy way
text = gutenberg.raw('carroll-alice.txt') #string
words = gutenberg.words('carroll-alice.txt') #list of strings (words)
sentences = gutenberg.sents('carroll-alice.txt') # list of lists of strings (sentences)
paragraphs = gutenberg.paras('carroll-alice.txt') # list of lists of lists of strings (paragraphs)

## the FreqDist class can be used to calculate the frequency distribution of a list of items. We can use the len() function to get the length of each word and sentence, and then pass the lengths to the FreqDist class to get the frequency distribution.
# Prepare text, remove punctuation and convert to lower case, then split the text into words and keep only words with length greater than 3.
lower_text = text.lower()
lower_text_no_punct = ''.join(letter for letter in lower_text if letter not in string.punctuation)
lower_words = lower_text_no_punct.split()
fdist_length_words = FreqDist(len(word) for word in words if len(word) > 3)
#use the plot() method of the FreqDist class to plot the frequency distribution of the length of words and sentences. The plot() method takes an optional argument to specify the number of bins to use for the histogram. We can also use the cumulative argument to specify whether to plot the cumulative frequency distribution or not.
plt.figure()
fdist_length_words.plot(10,cumulative=False)
plt.xlabel("Frequency of word lengths")
plt.ylabel("Frequency")
plt.show()
## the elaborated way, this function calculates the frequency distribution of the length of words in a text, removing punctuation and converting to lower case, and keeping only words with length greater than 3. The function returns a dictionary with the length of words as keys and the frequency of words with that length as values.
def word_length_distribution(txt,wordlength=3):
    # Renove punctuation and convert to lower case
    txt = text
    for letter in txt:
        if letter in string.punctuation:
            txt = txt.replace(letter, "")
    txt = txt.lower()
    # keep only words with length greater than 3
    wrds = []
    for wrd in txt.split():
        if len(wrd) > wordlength:
            wrds.append(wrd)
    # create a frequency distribution of the length of words using a dictionary, and the set() function to get the unique words in the text.
    unique_words = set(wrds)
    txt_fdist = dict()
    for wrd in unique_words:
        if len(wrd) not in txt_fdist.keys():
            txt_fdist[len(wrd)] = wrds.count(wrd)
        else:
            txt_fdist[len(wrd)] += wrds.count(wrd)
    return txt_fdist
# word length distribution for the text without punctuation and words with length greater than 3
text_fdist = word_length_distribution(text,3)
# with this method you have to make your own plot, using the matplotlib library. The keys of the dictionary are the lengths of the words, and the values are the frequencies of the words with that length. We can use the keys and values to create a bar chart using the bar() function of the pyplot module....
##
"""
2. Choose at least two different texts or a text corpus with more than one category from the NLTK module and compare them. Derive a measure of text complexity based on word and sentence length.
"""
# I added a folder into the project called textexamples with 60 text files, 30 of them are of low lexical complexity and 30 of them are of high lexical complexity. The texts are in Danish. The texts are named Stimulus_01_Easy.txt, Stimulus_02_Easy.txt, ..., Stimulus_30_Easy.txt, Stimulus_01_Hard.txt, Stimulus_02_Hard.txt, ..., Stimulus_30_Hard.txt. Each file has one paragraph and several sentences. The texts are in UTF-8 encoding.
# get the path to the folder in the format of the system.
cp_root = os.path.abspath('textexamples')
# add this path to the NLTK data path, so that the PlaintextCorpusReader can find the text files in the folder. The PlaintextCorpusReader class can be used to read a corpus of plain text files. The first argument is the path to the folder containing the text files, and the second argument is a regular expression pattern that matches the names of the text files. The encoding argument specifies the encoding of the text files.
nltk.data.path.append(cp_root)
Texts = PlaintextCorpusReader(cp_root, r".*\.txt",encoding="utf-8")
##
# lets compare the two categories of texts, Easy and Hard, by calculating the number of words, number of sentences, average word length and average sentence length for each text file in the corpus. We can use the words() and sents() methods of the PlaintextCorpusReader class to get the words and sentences of each text file, and then use the len() function to get the number of words and sentences. We can also use a list comprehension to calculate the average word length and average sentence length. Finally, notice the use of .2f to format the average word length and average sentence length to two decimal places.
textTypes = ["Easy", "Hard"]
for txtType in textTypes:
    for txtId in Texts.fileids():
        if txtType in txtId and "_quest.txt" not in txtId:
            num_words = len(Texts.words(txtId))
            num_sentences = len(Texts.sents(txtId))
            avg_word_length = sum(len(word) for word in Texts.words(txtId)) / num_words
            avg_sentence_length = num_words / num_sentences
            print(f"{txtType} - {txtId}:")
            print(f"Number of words: {num_words}")
            print(f"Number of sentences: {num_sentences}")
            print(f"Average word length: {avg_word_length:.2f}")
            print(f"Average sentence length: {avg_sentence_length:.2f}")
            print()
## Now we can construct a list of tuples with the text type and the number of words and sentences for each text file in the corpus. We can use a list comprehension to create the list of tuples, and then use the ConditionalFreqDist class of the nltk module to create a conditional frequency distribution of the number of words and sentences for each text type. The ConditionalFreqDist class takes a list of tuples as input, where each tuple contains a condition (in this case, the text type) and a value (in this case, the number of words or sentences). The ConditionalFreqDist class creates a frequency distribution for each condition, which we can use to compare the two categories of texts.

numbwords = [(txtType, len(Texts.words(txtId))) for txtType in textTypes for txtId in Texts.fileids() if txtType in txtId and "_quest.txt" not in txtId]
numbsentences = [(txtType, len(Texts.sents(txtId))) for txtType in textTypes for txtId in Texts.fileids() if txtType in txtId and "_quest.txt" not in txtId]
# the same but with for loops and if statements, this is more readable but less efficient
num_words = []
num_sentences = []
for txtType in textTypes:
    for txtId in Texts.fileids():
        if txtType in txtId and "_quest.txt" not in txtId:
            num_words.append((txtType, len(Texts.words(txtId))))
            num_sentences.append((txtType, len(Texts.sents(txtId))))



cdfw = nltk.ConditionalFreqDist(numbwords)
plt.figure()
cdfw.plot(cumulative=False)
plt.xlabel("Number of words per text")
plt.show()


cdfs = nltk.ConditionalFreqDist(numbsentences)
plt.figure()
cdfs.plot(cumulative=False)
plt.xlabel("Number of sentences per text")
plt.show()
##
# one layer deeper and we can create a list of tuples with the text type and the length of each word and sentence for each text file in the corpus. We can use a list comprehension to create the list of tuples, and then use the ConditionalFreqDist class of the nltk module to create a conditional frequency distribution of the length of words and sentences for each text type. The ConditionalFreqDist class takes a list of tuples as input, where each tuple contains a condition (in this case, the text type) and a value (in this case, the length of each word or sentence). The ConditionalFreqDist class creates a frequency distribution for each condition, which we can use to compare the two categories of texts.
lengthofwords = [(txtType, len(word)) for txtType in textTypes for txtId in Texts.fileids() if txtType in txtId and "_quest.txt" not in txtId for word in Texts.words(txtId)]
lengthofsentences = [(txtType, len(sentence)) for txtType in textTypes for txtId in Texts.fileids() if txtType in txtId and "_quest.txt" not in txtId for sentence in Texts.sents(txtId)]

cdflw = nltk.ConditionalFreqDist(lengthofwords)
plt.figure()
cdflw.plot(cumulative=False)
plt.xlabel("Length of words")
plt.show()


cdfls = nltk.ConditionalFreqDist(lengthofsentences)
plt.figure()
cdfls.plot(cumulative=False)
plt.xlabel("Length of sentences")
plt.show()


"""
3. Create a random text generator using the bigrams of a text and conditional frequency distributions choose a specific genre/style from the corpora found in the NLTK module. There is an example in ch2 of the NLTK book, try to expand on the example so that it does not get stuck repeating the same set of words.
"""

## Function for generating random text based on conditional frequencies of a corpus bigrams.
# the random package generates random integers and is used to randomly select the next word from the conditional distribution of bigrams. The function takes a list of words (text), a starting word (word), and the number of words to generate (num). It returns a list of generated words.
from random import randint as randi

def generate_model(text, word, num=15) -> str:
    new_sentence = []
    # make bigrams
    bg = nltk.bigrams(text)
    # conditional frequency distribution of bigrams
    cdfbg = nltk.ConditionalFreqDist(bg)
    # loop for desired number of words
    for i in range(num):
        # append the current word to the new sentence
        new_sentence.append(word)
        # get the most common words that follow the current word The most_common() method returns a list of tuples, where each tuple contains a word and its frequency count. The n parameter specifies the number of most common words to return. If there are no words that follow the current word, the loop continues to the next iteration without changing the current word.
        words_used_with = cdfbg[word].most_common(n=20)
        if words_used_with:
            indx = randi(0, len(words_used_with)-1)
            word = words_used_with[indx][0]
        else: # there are no words that follow the current word, so we can break the loop or choose a new random word from the text. Here we choose to break the loop.
            continue
    return " ".join(new_sentence)
#Select all hard and easy texts into two lists of words.
hard = [word.lower() for txtId in Texts.fileids() if "Hard" in txtId and "_quest.txt" not in txtId for word in Texts.words(txtId)]
easy = [word.lower() for txtId in Texts.fileids() if "Easy" in txtId and "_quest.txt" not in txtId for word in Texts.words(txtId)]
new_hard_sentence = generate_model(hard, 'de',10)

new_easy_sentence = generate_model(easy, 'de',10)

new_alice_sentence = generate_model(words, 'cat',20)



