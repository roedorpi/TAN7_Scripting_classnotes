"""
The following code is based on the NLTK book https://www.nltk.org/book/ that describes the use of the nltk package for language processing. The following are examples of code based on the first three chapters of the book.
The book is very good and gives a good overview of programming in python and processing language with a computer.
"""

##
import nltk # natural language tool kit.
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg') # back end for windows systems
#nltk.download()

## import text material from nltk.
from nltk.book import *

##  search for specific words in the one of the provided texts.
text5.concordance("lol")
text5.similar("lol")
text5.count('lol')
text5.common_contexts('lol')

# make a plot of where in the text each word appears.
text5.dispersion_plot(["fearless", "borring", "kill", "kitty", "lol"])
plt.show()

## Word frequency distribution, that is, what is the frequency of appearance of each word in the text.
fdist5 = FreqDist(text5)
print(fdist5)
# show most commom words
fdist5.most_common(50)
fdist5.plot(50, cumulative=True)
plt.show()

## select words based on their length
V = set(text1)
long_words = [w for w in V if 10 < len(w) < 20]
print(sorted(long_words))

## select based on length and frequency
fdist1 = FreqDist(text1)
frequent_long_words = [w for w in V if len(w)>10 and fdist1[w] > 10]
print(sorted(frequent_long_words))

## find collocations and bigrams
# words that are commonly used together
coloct1 = text1.collocations()
# bigrams every combination of two consecutive words
bgt1 = list(bigrams(text1))

## finding the index of elements in a list using the iterator enumerate() that creates a list of tuples containing an index and the list value.
index_of_the_word_the = [i for i,w in enumerate(sent3) if w == 'the']
print(index_of_the_word_the)

## all words starting with letter b in text5

words_starting_with_b = [w for w in text5 if w.startswith('b')]
print(sorted(set(words_starting_with_b)))

## functions for vocabulary size and word usage percentage, function definitions need to be read by the interpreter before they can be used.

def vocab_size(txt) -> int:
    return len(set(txt))

def word_usage(word, txt) -> float:
    fd = FreqDist(txt)
    fd.freq(word)
    return fd.freq(word)*100
## Import plain text corpus. This example is based on 60 paragraphs of random topics. 30 are of low lexical complexity
# and 30 are of high lexical complexity. The texts are in Danish.
from nltk.corpus import PlaintextCorpusReader
# folder with texts
corpus_root = r".\textexamples"
# name of file pattern
filepattern = r'Stimulus.*.txt'
wordlists = PlaintextCorpusReader(corpus_root,filepattern)
fileID = wordlists.fileids()
## Get an overview of the content: calculate average word length, average sentence length and average word repetition
# for each text file in the corpus
Summary = []
for i,fil in enumerate(wordlists.fileids()):
    if 'quest' not in fil:
        num_chars = len(wordlists.raw(fil))
        num_words = len(wordlists.words(fil))
        num_sents = len(wordlists.sents(fil))
        num_vocab = len(set(w.lower() for w in wordlists.words(fil)))
        aver = [num_chars/num_words, num_words/num_sents, num_words / num_vocab]
        if 'Hard' in fil: condition = 2
        else: condition = 1

        aver.append(condition)
        Summary.append(aver)
## Use numpy arrays to calculate means and standard deviations, for the two levels of lexical diversity
Average = np.array(Summary)

Ave_hard = Average[Average[:,3]==2,:-1].mean(axis=0)
Ave_easy = Average[Average[:,3]==1,:-1].mean(axis=0)
Std_hard = Average[Average[:,3]==2,:-1].std(axis=0)
Std_easy = Average[Average[:,3]==1,:-1].std(axis=0)
print(Ave_hard, Ave_easy, Std_hard, Std_easy)

## get the fileID for the two conditions, ignoring unwanted files, the ones with 'quest' in the file name
fileID_hard = [i for i in fileID if 'Hard' in i and 'quest' not in i]
fileID_easy = [i for i in fileID if 'Easy' in i and 'quest' not in i]
## Conditional frequency distribution by type (hard, easy) for word length
cdf = nltk.ConditionalFreqDist(
    (Type[0][9:13], len(word))
    for Type in [fileID_hard, fileID_easy]
    for word in wordlists.words(Type))
cdf.plot(cumulative=False)
plt.title('Conditional Frequency Distribution for word length')
plt.xlabel('Word length')
plt.ylabel('Counts')
plt.show()

## Conditional frequency distribution by type (hard, easy), taking into account only words of a specific length and
# frequency of occurence.
fdist = nltk.FreqDist(wordlists.words())
cdf = nltk.ConditionalFreqDist(
    (Type[0][9:13], word)
    for Type in [fileID_hard, fileID_easy]
    for word in [w.lower() for w in wordlists.words(Type)]
    # for words between 5 and 12 characters long and with frequency count between 20 and 40
    if 12 > len(word) >= 5 and  40>fdist[word]>20)
cdf.plot(cumulative=False)
plt.title('CDF for word of length greater than 5 with counts between 20 and 40')
plt.xlabel('Word length')
plt.ylabel('Counts')
plt.show()

## Generate collocations for a corpous. Collocations are pairs of words that appear after each other more that usually, i.e. red wine or cold beer
# Define function to find collocations
def find_collocations(text) -> list:
    collocations = []
    # generate bigrams of text input. bigrams are pairs of words that appear together.
    bg = nltk.bigrams(text)
    # make the conditional frequency distribution for each word of the text using the bigrams
    cfdbg = nltk.ConditionalFreqDist(bg)
    # go through each word and find the 10 most common bigrams for that word
    for w in text:
        words = cfdbg[w].most_common(n=10)
        if words:
            # check is the words of the bigram are longer that 3 characters and that they occur at least three times
            common_bigrams = [(w,wd[0]) for wd in words if wd[1] >=3 and len(w)>3 and len(wd[0])>2]
            if common_bigrams:
                # add the bigrams as tuples in the collocation list
                for bg in common_bigrams:
                    collocations.append(bg)
    # sort and eliminate repetitions
    collocations = sorted(set(collocations))
    return collocations

# Make all text lower case and remove single character words (also commas exclamation or question marks and periods)
hard = [w.lower() for w in wordlists.words(fileID_hard) if len(w)>5]
easy = [w.lower() for w in wordlists.words(fileID_easy) if len(w)>5]
# apply the function to the desired text
hard_collocations = find_collocations(hard)
easy_collocations = find_collocations(easy)
## Function for generating random text based on conditional frequencies of a corpus bigrams.
from random import randint as randi
def generate_model(text, word, num=15) -> list:
    new_sentence = []
    # make bigrams
    bg = nltk.bigrams(text)
    # conditional frequency distribution of bigrams
    cdfbg = nltk.ConditionalFreqDist(bg)
    # loop for desired number of words
    for i in range(num):
        # add space after the word
        new_sentence.append(word)
        words = cdfbg[word].most_common(n=5)
        if words:
            indx = randi(0, len(words)-1)
            word = words[indx][0]
        else:
            continue
    return new_sentence
#
new_hard_sentence = generate_model(hard, 'de',10)

new_easy_sentence = generate_model(easy, 'de',10)

## stop words, these are plumbing words of the text, they are there for gramatical purposes but do not contribute to the
# meaning.

def remove_stopwords(text,language) -> list:
    stopwords = nltk.corpus.stopwords.words(language)
    return [w for w in text if w.lower() not in stopwords]

hard_clean = remove_stopwords(hard,'danish')

