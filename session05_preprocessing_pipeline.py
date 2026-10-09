"""Session05: NLP preprocessing pipeline with stopword removal."""

import nltk, re, pprint
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
from urllib import request



def tokenize(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.split()


def remove_stopwords(tokens):

    stop_words = set(stopwords.words("english"))
    return [token for token in tokens if token not in stop_words]


def filtered_tokens(token_: list, min_length: int = 3):
    tokens = remove_stopwords(token_)
    return [token for token in tokens if len(token) >= min_length]


def word_frequencies(token_: list):
    return Counter(token_)


if __name__ == "__main__":

    url = "http://www.gutenberg.org/files/2554/2554-0.txt"
    response = request.urlopen(url)
    raw_text = response.read().decode("utf-8")
    #find the index of "PART I" and the end of the book to extract the main content
    part_i_index = raw_text.find("PART I")
    end_of_book_index = raw_text.find("*** END OF THE PROJECT GUTENBERG EBOOK 2554 ***")
    # extract the main content of the book
    text_    = raw_text[part_i_index:end_of_book_index]
    #tokenize the text using different methods and print the results
    raw_tokens = tokenize(text_)
    cleaned_tokens = filtered_tokens(raw_tokens, min_length=1)
    nlp_tokens = word_tokenize(text_)
    cleaned_Text = nltk.Text(cleaned_tokens)
    nlp_Text = nltk.Text(nlp_tokens)