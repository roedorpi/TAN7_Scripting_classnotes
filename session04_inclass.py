##
from nltk.corpus import gutenberg as gut
text = gut.sents("carroll-alice.txt")
def sentence_extraction(txt, keyword):

    fout = open(f"{keyword}.txt", "w")
    count = 0
    for sentence in txt:
        if keyword in sentence:
            fout.write(" ".join(sentence) + "\n")
            count += 1
    fout.close()
    print(f"Found {count} sentences containing the word '{keyword}'.")

sentence_extraction(text, keyword="cat")
