"""
1. Write a program that can:
- create a list of 10 items
- create a set with 10 items
- create a dictionary with 10 key-value pairs
- create a loop that iterates over the list, set and dictionary and prints each item
- use a list comprehension to create a new list with every other item from the original list
- create a list of long words (more than 5 characters) from a given text and print them
"""
##
import re

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
##
mylist = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
myset = {"Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Kiwi", "Lemon"}
mydict = {mylist[0]:3, mylist[1]:5, mylist[2]:7, mylist[3]:2, mylist[4]:9, mylist[5]:1, mylist[6]:4, mylist[7]:6, mylist[8]:8, mylist[9]:0}

for item in mylist:
    print(item)

for item in myset:
    print(item)

for key, value in mydict.items():
    print(key, value)

for item in mydict.values():
    print(item)


newlist = [item for i,item in enumerate(mylist) if i % 2 == 0]
print(newlist)

newDict = {k:val for k,val in enumerate(mylist)}

"""
2. Use a dictionary to store a corpus of texts, where the keys are the document names and the values are the text content.
- Use the corpus and what you have learned to print out some basic statistics about the texts, such as the number of words, number of unique words, and average word length, lexical complexity, etc.
- Create the frequency distribution of the words in the corpus and print out the most common words. Do the same for each document in the corpus and compare the results. Are there any evident differences in the vocabulary used in each document?
- Create the frequency distribution of the words in the corpus that are larger than 5 characters and print out the most common words. Do the same for each document in the corpus and compare the results. Are there any evident differences in the vocabulary used in each document?

"""
##
with open("wonderland.txt","r",encoding="utf-8") as f:
    text = f.read()

text_longwords = [word for word in re.findall(r"[A-Za-z']+", text) if len(word) > 5]

##
chapter1 = text.split("CHAPTER I.")[2].split("CHAPTER II.")[0]
chapter2 = text.split("CHAPTER II.")[2].split("CHAPTER III.")[0]
chapter3 = text.split("CHAPTER III.")[2].split("CHAPTER IV.")[0]
chapter4 = text.split("CHAPTER IV.")[2].split("CHAPTER V.")[0]
# Alice in wonderland corpus only the first 4 chapters
AliceInWonderland = {
    "chapter1": chapter1,
    "chapter2": chapter2,
    "chapter3": chapter3,
    "chapter4": chapter4
}
##
def textstat(inText, n=5):
    tokens = [word for word in re.findall(r"[A-Za-z']+", inText.lower()) if len(word) > n]
    outdict = dict()
    outdict["nwords"] = len(tokens)
    outdict["nsentences"] = len(re.split(r"[.!?]+", inText.strip()))
    wordFreqDist = dict()
    for word in tokens:
        wordFreqDist[word] = wordFreqDist.get(word, 0) + 1
    outdict["wordFreqDist"] = wordFreqDist
    return outdict


def plot_top_words(stat_dict, n=10):
    """Plot the top n words for each section stored in a StatDict-style dictionary."""
    num_sections = len(stat_dict)
    fig, axes = plt.subplots(num_sections, 1, figsize=(12, 3.2 * num_sections), squeeze=False)

    for ax, (label, stats) in zip(axes.flat, stat_dict.items()):
        items = sorted(stats["wordFreqDist"].items(), key=lambda item: (-item[1], item[0]))[:n]
        words = [word for word, _ in items]
        counts = [count for _, count in items]

        ax.bar(words, counts, color="steelblue")
        ax.set_title(f"Top {n} words in {label}")
        ax.set_ylabel("Frequency")
        ax.tick_params(axis="x", rotation=45)
        if max(counts) < 25:
            ax.set_ylim(0, 25)


    plt.tight_layout()
    # output_path = "alice_top_words.png"
    # fig.savefig(output_path, dpi=150, bbox_inches="tight")
    # print(f"Saved plot to {output_path}")
    plt.show()


StatDict = dict()
for key in AliceInWonderland.keys():
    StatDict[key] = textstat(AliceInWonderland[key], n=5)

StatDict["all"] = textstat(text, n=10)
print(StatDict)
plot_top_words(StatDict)
