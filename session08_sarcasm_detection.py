#!/usr/bin/env python
# coding: utf-8

# ## sarcasm detection
# source: https://thecleverprogrammer.com/2021/08/24/sarcasm-detection-with-machine-learning/


# https://scikit-learn.org/stable/user_guide.html
# section 6.2.3 Text feature extraction
# section 3.1 Cross Validation
# section 1.9 Naive Bayes
# %%


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from wordcloud import WordCloud
from matplotlib import pyplot as plt

#load data
data = pd.read_json("Sarcasm.json", lines=True)
print(data.head())


# Rename categorical variable
data["is_sarcastic"] = data["is_sarcastic"].map({0: "Not Sarcasm", 1: "Sarcasm"})
print(data.head())


# Keep only the headline and the classification
data = data[["headline", "is_sarcastic"]]
# change into numpy arrays for vectorization
x = np.array(data["headline"])
y = np.array(data["is_sarcastic"])
# initialize the vectorizer
cv = CountVectorizer()
# transform the data, the list of sentences becomes a matrix where each row represent sentences and each and there is a column for every word in the data. The value in each cell represents the number of times a given word appears in that sentence. Parameters of the vectorization can be done in the initialization of the vectorizer... see the documentation.
X = cv.fit_transform(x)
# split the data in training and test.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Initialize the language model
model = BernoulliNB()
# train the model with the training set
model.fit(X_train, y_train)
# test the model with the test set
print(model.score(X_test, y_test))

# Get input from user
user = input("Enter a Text: ")
# process input to feed it to the model
new_data = cv.transform([user]).toarray()
output = model.predict(new_data)
print(output)


## Make word clouds of sarcastic and non sarcastic sentences using different vectorizer setting.

sarcastic_sentences = data[data['is_sarcastic'] == 'Sarcasm'].headline.to_list()
not_sarcastic_sentences = data[data['is_sarcastic'] == 'Not Sarcasm'].headline.to_list()

cv2 = CountVectorizer(analyzer='word', token_pattern="[a-z]{5,20}", decode_error='replace')
cv3 = CountVectorizer(analyzer='word', ngram_range=(4, 4), decode_error='replace')


x2_s = cv2.fit_transform(sarcastic_sentences)
ngrams2_s = cv2.get_feature_names_out()
ngrams2_s_freq = sum(x2_s.toarray())
vocab2_s = {}
i = 0
for k in ngrams2_s:
    vocab2_s[k] = ngrams2_s_freq[i]
    i += 1

x2_ns = cv2.fit_transform(not_sarcastic_sentences)
ngrams2_ns = cv2.get_feature_names_out()
ngrams2_ns_freq = sum(x2_ns.toarray())
vocab2_ns = {}
i = 0
for k in ngrams2_ns:
    vocab2_ns[k] = ngrams2_ns_freq[i]
    i += 1


x3_s = cv3.fit_transform(sarcastic_sentences)
ngrams3_s = cv3.get_feature_names_out()
ngrams3_s_freq = sum(x3_s.toarray())
vocab3_s = {}
i = 0
for k in ngrams3_s:
    vocab3_s[k] = ngrams3_s_freq[i]
    i += 1


x3_ns = cv3.fit_transform(not_sarcastic_sentences)
ngrams3_ns = cv3.get_feature_names_out()
ngrams3_ns_freq = sum(x3_ns.toarray())
vocab3_ns = {}
i = 0
for k in ngrams3_ns:
    vocab3_ns[k] = ngrams3_ns_freq[i]
    i += 1

#
wordcloud = WordCloud()

wordcloud.generate_from_frequencies(vocab2_s)
# plot using matplotlib.pyplot
plt.figure(1)
plt.subplot(141)
plt.imshow(wordcloud)
plt.show()
plt.axis('off')


wordcloud.generate_from_frequencies(vocab2_ns)
# plot using matplotlib.pyplot
plt.subplot(142)
plt.imshow(wordcloud)
plt.show()
plt.axis('off')



wordcloud.generate_from_frequencies(vocab3_s)
# plot using matplotlib.pyplot
plt.subplot(143)
plt.imshow(wordcloud)
plt.show()
plt.axis('off')


wordcloud.generate_from_frequencies(vocab3_ns)
# plot using matplotlib.pyplot
plt.subplot(144)
plt.imshow(wordcloud)
plt.show()
plt.axis('off')


