#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# write your simulation code here
import random
import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

def ProbabilitySimulation(tries, noEntries, probability):
    # matching variables with parameters for further use
    tries = tries
    noEntries = noEntries
    probA = probability

    satisfiedEntry = 0

    count = 0

    # under tries
    while count < tries:
        # empty array each iteration
        entriesResult = []

        k = 0

        # for each random entry we want to have sets of 7
        while k < noEntries:
            # a random probability from 0 to 1 to which we will compare with the probability of A to happen
            randomEntry = random.random()
            # if the random probability is equal or under 'probA' (the probability of event A occurring) 
            if randomEntry <= probA:
                # we conclude event A occured and append it to the iteration array
                entriesResult.append("A")
            else: 
                # if the probability is higher, we conclude it is not A, and we signal it in a form
                entriesResult.append("notA")
            k += 1

        # compare the findings from the array
        # assuming that the prompt requires the order as well
        # if we find the set of 7 where 3 entries satisfy A and 4 that don't, we increment our 'satisfiedEntry' variable
        if entriesResult[0] == "A" and entriesResult[1] == "A" and entriesResult[2] == "A" and entriesResult[3] == "notA" and entriesResult[4] == "notA" and entriesResult[5] == "notA" and entriesResult[6] == "notA":
            satisfiedEntry += 1


        count += 1

    # since the prompt asks for a probability of such satisfied entries, we divide the satisfied entries by the overall number of tries
    prob = satisfiedEntry/tries
    return prob

print(ProbabilitySimulation(1000, 7, 0.56))

