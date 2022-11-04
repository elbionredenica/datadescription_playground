#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

# write your function for the standard deviation here
# calculating the standard variation of average ratings

def standard_deviation(dataset):
    # we start by pushing our elements into an array
    allRatings = []
    l = len(dataset)
    
    for i in range(l):
        allRatings.append(dataset.iloc[i])
    
    # although the lenght of this array should be the same as the whole dataset's, it's a good practice to distinguish it 
    n = len(allRatings)
    
    # we declare all the variables needed to recreate the formula
    standardDeviation_numerator = 0 # "numerator" as in divisions
    ratings = 0
    
    # we recreate the steps of finding the mean as we're going to need it within the formula
    for i in range(n):
        ratings += allRatings[i]
    
    mean = ratings/n
    
    # this is what the numerator is equal with from the formula of SD
    for i in range(n):
        standardDeviation_numerator += (allRatings[i] - mean)**2
    
    # this formula only gives us the variance
    variance = (standardDeviation_numerator / (n - 1))
    
    # SD is the square root of variance
    standardDeviation = variance**0.5
    
    return standardDeviation

print(standard_deviation(df.average_rating))

