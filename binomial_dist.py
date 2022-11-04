#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import stats from the scipy library
from scipy import stats
import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

# the probability of the event occurring
probA = 0.56
# number of trials
noA = 7
# success rate (number of successes within the given trials)
succA = 3

# the calculation using the stats' binomial function
probSatA = stats.binom.pmf(succA, noA, probA)

# the calculation using the binomial formula, where the first part (112/200)**3 * (88/200)**4 is the sampling with replacement, so we are replacing an element each time we choose one. The second part is the combinatorics part of the formula 7^C4: 7!/3!(7-3)! = 5040/(3!*4!) = 5040/144 = 35
probability = (((112/200)**3 * (88/200)**4) * 35)

# the results should match
print(probSatA, probability)

