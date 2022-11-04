#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

# write your function for the range here
# the range of publication dates
def Range(dataset):
    # the structure for this prompt is simple: (1) we create an array with our values and push them into it, (2) sort it, (3) and the first and the last value should give us the range
    allRatings = []
    n = len(dataset)

    # (1)
    for i in range(n):
        allRatings.append(dataset.iloc[i])
    
    # (2)
    allRatings.sort()
    
    # (3) -- [-1] returns the last element of the array
    return allRatings[0], allRatings[-1]

print(Range(df.ratings_count))

