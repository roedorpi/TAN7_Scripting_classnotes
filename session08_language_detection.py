#!/usr/bin/env python
# coding: utf-8

# ## language detection
# source: https://thecleverprogrammer.com/2021/10/30/language-detection-with-machine-learning/
#

# https://scikit-learn.org/stable/user_guide.html
# sections 6.2.3 # text feature extraction "the bag of words"
# sections 3.1 Cross Validation
# section 1.9 Naive Bayes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from wordcloud import WordCloud

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/dataset.csv")
print(data.head())


# %%
data.isnull().sum()


# %%
data["language"].value_counts()


# %%
x = np.array(data["Text"])
y = np.array(data["language"])



cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.33,
                                                    random_state=42)


# %%
model = MultinomialNB()
model.fit(X_train, y_train)
model.score(X_test, y_test)


# %%
user = input("Enter a Text: ")
user_data = cv.transform([user]).toarray()
output = model.predict(user_data)
print(output)

# wordcloud for english sentences
# get all sentences in english and put them in a list.
eng_sentenses = data[data["language"].values == output[0]].Text.to_list()
# prepare a countvectorizer to get unique features (words in this case) and their occurrence

x = cv.fit_transform(eng_sentenses)
ngrams = cv.get_feature_names_out()

# get the frequency of the ngrams. The toarray() method returns the frequency of each ngram for each sentence in a list of list, each list corresponding to each sentence. By summing across lists we can obtain the frequency of occurence for each ngram across all sentences.
ngrams_freq = sum(x.toarray())

vocab = {}
i = 0
for k in ngrams:
    vocab[k] = ngrams_freq[i]
    i += 1

# create the word cloud, using the dictionary created above
# initialize word cloud
wordcloud = WordCloud()
# generate word cloud with dictionary
wordcloud.generate_from_frequencies(vocab)
# plot using matplotlib.pyplot
plt.imshow(wordcloud)
plt.show()
plt.axis('off')
