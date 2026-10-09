##
from nltk.corpus import gutenberg as gut
text = gut.sents("carroll-alice.txt")
def sentence_extraction(txt, *keywords):
    count = 0
    outputdict = {}
    for sentence in txt:
        for keyword in keywords:
            if keyword not in outputdict.keys():
                outputdict[keyword] = []
            if keyword in sentence:
                outputdict[keyword].append(" ".join(sentence))
            count += 1

    print(f"Found {count} sentences containing the words '{', '.join(keywords)}'.")
    return outputdict

results = sentence_extraction(text, "cat", "hat", "Alice")
