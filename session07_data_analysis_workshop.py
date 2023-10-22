#!/usr/bin/env python
# coding: utf-8

# # data analysis workshop

# Gamble, T., & Walker, I. (2016). Wearing a Bicycle Helmet Can Increase Risk Taking and Sensation Seeking in Adults. <i>Psychological Science, 27</i>(2).
# 
# original paper: https://doi.org/10.1177/0956797615620784
# 
# original data downloaded from: https://osf.io/eky4s/
# 
# PLEASE NOTE: the dataset you are using today has been altered for the purposes of this exercise. 


# ## variables:
# 
# ID: Participant identification number
# 
# Condition: Which condition the participant was in: 1=helmet, 2=cap
# 
# Age: Age in years
# 
# Sex: Gender of the participant: 1=male, 2=female
# 
# STAI pre: State Trait Anxiety Inventory Y state anxiety total before wearing the eye-tracker
# 
# SSS total: Sensation Seeking Scale score
# 
# BART: Balloon Analogue Risk Task adjusted mean (mean number of pumps on trials where the balloon did not burst); 
# assume that MINIMUM BART score = 100; MAXIMUM = 8500
# 
# STAI during: State Trait Anxiety Inventory Y state anxiety total whilst wearing the eye-tracker
# 
# STAI post: State Trait Anxiety Inventory Y state anxiety total after wearing the eye-tracker
# 
# Cycling frequency: How often does the participant cycle: 1=Never, 2=Rarely, 3=At least once a month, 4=At least once a week, 
# 5=At least two to four times a week, 6=Five times a week or more
# 
# Helmet use likelihood: How often does the participant wear a cycle helmet: 0=don’t cycle, 1=never - 7=always
# 

# ## import modules

import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# ### load data

# read in data file as a data frame
helmets_df = pd.read_csv('helmets_data.csv', delimiter=";")

# print our data
helmets_df


# ## data cleaning

# ### exploring data

# first, let's get general statistics on all the variables.
# do you notice any potentially problematic issues?
helmets_df.describe()
helmets_df.groupby('Condition').agg({'Condition':['count']})


# #### removing potential duplicates
# why are duplicate data points a problem?
helmets_df = helmets_df.drop_duplicates()


# #### screening for missing data
# Do we have any empty cells (missing values) in our data? 
# we see that we have some potentially missing values, is that true?
helmets_df.isnull().any()


# Is that a problem? How is an empty cell different from 0?
# remove rows with empty values
helmets_df = helmets_df.dropna(axis=0, how='any')


# #### locating and removing "illegal" values

# age: what are "illegal" age values? Do we have any of them present in our data?
# age counts
helmets_df.groupby('Age').agg({'Age':['count']})
# drop rows where cells meet conditions
helmets_df = helmets_df[(helmets_df.Age>=17) & (helmets_df.Age<=65)]

# sex: what are the "illegal" sex values? Do we have any of them present in our data?
# sex counts
helmets_df['Sex'].value_counts()
# drop rows where cells meet conditions
helmets_df = helmets_df[(helmets_df.Sex==1) | (helmets_df.Sex==2)]

# BART scores: what are the "illegal" values?
# drop rows where cells meet conditions
helmets_df = helmets_df[(helmets_df.BART>100) & (helmets_df.BART<8500)]

# cycling frequency and helmet use likelihood: what are the "illegal" value pairs?
# find rows that specify conditions and drop them
index_name = helmets_df[(helmets_df.Cycling_Frequency==1) & (helmets_df.Helmet_Use_Likelihood!=0)].index
helmets_df.drop(index_name, inplace=True)

helmets_df

# save our cleaned data file!
helmets_df.to_csv('outFile.csv')


# ## data plotting

# ### scatterplots
sns.scatterplot(data=helmets_df, x='BART', y='SSS_total', hue='Condition', style='Condition')

cap_df = helmets_df[helmets_df.Condition == 1]
hel_df = helmets_df[helmets_df.Condition == 2]

sns.lmplot(x='BART', y='SSS_total', data=cap_df, ci=None).fig.suptitle("condition = cap")
sns.lmplot(x='BART', y='SSS_total', data=hel_df, ci=None).fig.suptitle("condition = helmet")

sns.lmplot(x='BART', y='SSS_total', hue='Condition', data=helmets_df)

sns.jointplot(x='BART', y='SSS_total', data=hel_df, kind="reg").fig.suptitle("condition = helmet")
sns.jointplot(x='BART', y='SSS_total', data=cap_df, kind="reg").fig.suptitle("condition = cap")

sns.lmplot(x="BART", y="SSS_total", hue="Condition", col="Sex", data=helmets_df);


# ### histograms
sns.displot(helmets_df, x='BART',bins=15, kde=True)

sns.displot(helmets_df, x='BART', hue='Condition', kde=True)

sns.displot(helmets_df, x='BART', hue='Condition', multiple='dodge',bins=10, col='Sex', kde=True)


# ### kernel density estimation
sns.displot(helmets_df, x='BART', hue='Condition', kind="kde", multiple='stack')

# ### boxplot
sns.catplot(data=helmets_df, x="Condition", y="BART", kind="bar")

sns.catplot(data=helmets_df, x="Condition", y="BART", kind="box")

sns.catplot(data=helmets_df, x="Condition", y="BART", kind="box", hue='Sex')

print('done')