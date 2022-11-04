#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

# # # # NOTE: I use variables from cross files: for reference check other .ipynb as well # # # #
# use this cell to help with the calculations for 1.2
# # P(A) = number of entries with event A occuring
probabilityA = textReviewsUnder50/n
print("The probability of A:", probabilityA)

# # P(B) = number of entries with event B occuring
probabilityB = TheCounter/n
print("The probability of B:", probabilityB)

# # P(A and B) 
# # The number of cases these events occur together over all cases
probabilityAandB = AandB/n
print("The probability of A and B:", probabilityAandB)

# # 2. P(A or B)
# # P(A or B) = P(A) + P(B) - P(A and B)
# We have the probabilities of all variables from the previous calculations to use
probabilityAorB = probabilityA + probabilityB - probabilityAandB
print("The probability of A or B:", probabilityAorB)

# # 3. P(A|B) - read: probability of A given B
# # P(A|B) = P(A and B) / P(B) : this is the formula
probabilityAgivenB = probabilityAandB / probabilityB
print("The probability of A given B: ", probabilityAgivenB)

