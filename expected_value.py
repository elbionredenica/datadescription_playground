#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

probA = 0.56
noEntries = 7

def my_EV(X,probX):
    # this function returns the EV of a random variable X
    # input list of outcomes of the random variable X = [x1,...,xN]
    # and the probabilities probX = [P(x1),...P(xN)]
    sumtotal = 0
    total = 0
    # for each entry, we calculate the probability of that entry to happen, which is the same for all events A (0.56) and we've named it "probA"
    for i in range(X):
        # since this is going to be iterated and the number of entries is fixed, the sumtotal for an iteration is going to be the proability of the event happening itself
        sumtotal += 1 * probX
    
    return sumtotal

print(my_EV(noEntries, probA))
# in our case given the circumstances, this can also be calculated simply by multiplying the probability of A occurring with the number of entries
print(probA * noEntries)

