#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

# write your function for the mode here
# example: calculating mode of book languages

def Mode(dataset):
    # creating a dictionary to store our frequencies of book languages from the dataset
    frequencies = {}

    # iteration
    for i in dataset:
        frequencies[i] = frequencies.get(i, 0) + 1 # .get() method returns the value of the item with the specified key. + 1 because we increment if it's found in there as a frequency (occurrence)

    # .max() simply returns the largest value, and we're looking for it in our frequencies dictionary, then storing it in the variable "mode" 
    mode = max([freq for freq in frequencies.values()])
    
   
    
    # checking for keys from the frequencies array that match the max value from the previous mode variable.
    # note that we should be able to handle multimodes, so creating an array with the purpose of pushing all items that fulfill the conditions seems as a reasonable thing to do
    modes = []
    for key in frequencies.keys():
        if frequencies[key] == mode:
            modes.append(key)
    
    return modes

print(Mode(df.language_code))

