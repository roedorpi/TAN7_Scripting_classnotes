#!/usr/bin/env python
# coding: utf-8

# # The Datasaurus Dozen visualization
# 
# source: https://doi.org/10.1145/3025453.3025912

# %%
# step 1: load modules

import pandas as pd
import seaborn as sns

# %%
# step 2: load and check data
# 
# How are the data structured in the file?

datasaurus_data = pd.read_csv('DatasaurusDozen.csv', delimiter="\t")
datasaurus_data

# %%
# step 3: descriptive statistics grouped by dataset
# 
# What do you notice about the descriptive statistics for each dataset? How do those datasets compare?

grouped = datasaurus_data.groupby('dataset')
grouped.agg({'x': ['count', 'mean', 'std'], 'y': ['count', 'mean', 'std']})

# %%
# step 4: scatterplot of all data, regardless of dataset
# 
# What does this scatterplot tell us about our data?

sns.scatterplot(data=datasaurus_data, x='x', y='y')

# %%
# step 5: scatterplot of all data, color-coded by dataset
# 
# What does this scatterplot tell us about our data?

sns.scatterplot(data=datasaurus_data, x='x', y='y', hue="dataset")


# %%
# step 6: individual scatterplot of single dataset, <i>away</i>
# 
# What does this scatterplot tell us about our data?

sns.scatterplot(data=grouped.get_group("away"), x='x', y='y')

# %%
# step 7: individual scatterplots of all datasets
# 
# What does this scatterplot tell us about our data?

sns.relplot(data=datasaurus_data, x='x', y='y', col='dataset', col_wrap=3)
