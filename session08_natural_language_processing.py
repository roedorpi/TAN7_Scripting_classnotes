##
import nltk
import numpy as np
import nltk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg', force=True)
from nltk.corpus import *
from nltk.book import *
##
text4.concordance('freedom')


text4.dispersion_plot(["man","people","freedom","arms","woman"])
plt.show()


##
# find maches and show their context
text1.concordance('monster')
# find words that are used in similar contexts
text1.similar('monster')
# plot the placement of the words in the text
text1.dispersion_plot(["whale","monster","harpoon","captain","man","leviathan"])
plt.show()
# Generate text based on the style of the source text
text1.generate()

## Counting contents
number_of_items= len(text1)
bag_of_words = sorted(set(text1))
number_of_unique_items = len(set(text1))

lexical_richness = number_of_unique_items/number_of_items

average_word_use = number_of_items/number_of_unique_items

occurance_of = text1.count('man')
percentage_of_text = 100 * occurance_of/number_of_unique_items

## Frequency distributions
fdist1 = FreqDist(text1)
# common words
fdist1.most_common(50)
fdist1.plot(50,cumulative=True,percents=True)
plt.show()

# least common frequency of 1
fdist1.hapaxes()

# words greater than a certain number of characters
Vocab = set(text1)
long_words = [w for w in Vocab if len(w) >15]
print(sorted(long_words))

# words greater than a certain number of characters
long_frequent_words = [w for w in Vocab if len(w) >10 and fdist1[w] > 10]
print(sorted(long_frequent_words))




## Collocations and Bigrams
# all consecutive words in the text
bigrams_text1 = list(bigrams(text1))
# all consecutive words larger than 4 characters
long_bigrams = [b for b in bigrams_text1 if len(b[0]) > 4 and len(b[1]) > 4]

bigrams_count = FreqDist(long_bigrams)
bigrams_count.plot(50)
plt.show()