"""Session 5: Visualizing word distributions and text patterns."""

from collections import Counter
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import string

# basic simple tokenizer that splits text into words based on whitespace and converts to lowercase and eliminates punctuation.
def tokenize(text: str):
    text = "".join([c for c in text if c not in string.punctuation])
    return text.lower().split()

def top_words(text: str, n: int = 10):
    counts = Counter(tokenize(text))
    return counts.most_common(n)


def make_frequency_bar_chart(text: str):

    counts = Counter(tokenize(text))
    labels, values = zip(*counts.most_common(10))
    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.title("Top 10 words")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def make_wordcloud(text: str):

    wc = WordCloud(width=900, height=500, background_color="white")
    wc.generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":


    sample_text = gutenberg.raw("carroll-alice.txt")

    print("Top words:")
    for word, count in top_words(sample_text, 10):
        print(f"{word}: {count}")

    make_frequency_bar_chart(sample_text)
    make_wordcloud(sample_text)
