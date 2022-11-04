#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

# write your function for the mean here
# example: calculating the mean of 'average rating'

def Mean(dataset):
    n = len(dataset) # the length of the Goodreads dataset
    sum = 0 
    # we count each element's value in the dataset 
    for i in range(n): 
        sum += dataset.iloc[i] # .iloc because we're going to need specific integer location
    
    # the mean is equal to the cell values of each entry divided by the number of entries
    mean = sum/n
    
    # rounding to 2 since we have all our ratings with two decimals
    return round(mean, 2)

# df.[columnName] specifies a column in the DataFrame we want to fetch
print(Mean(df.average_rating))

