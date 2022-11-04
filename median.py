#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

# write your function for the median here
# example: calculating the median of the numbers of pages

def Median(dataset):
    n = len(dataset)
    # for easier manipulation I will store all values in an array
    AllNumPages = []
    
    for i in range(n):
        AllNumPages.append(dataset.iloc[i]) # .append() pushes elements into the array, and this iteratively pushes every page number from the entry
    
    # to find the median we must have our list sorted (.sort()).
    AllNumPages.sort()
    
    # the median is the middle value of a sorted list
    # if the number of list elements is even (n % 2 == 0), we take the arithmetic mean of the two middle values
    if n % 2 == 0:
        oddMedianDividedVar1 = AllNumPages[n//2 - 1]
        oddMedianDividedVar2 = AllNumPages[n//2]
        return (oddMedianDividedVar1 + oddMedianDividedVar2) / 2
    # else, the number of list elements is odd and we simply take the middle value 
    else:
        return AllNumPages[n//2]
    
print(Median(df.num_pages))

