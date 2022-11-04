#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# alternative solution which is essentially the same in terms of simulation
# the difference is that this fetches samples from the dataset
# the drawback of this code is its time complexity, but by definition this is a simulation so I guess it makes sense
import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]


def simulateProbability(tries, noEntries):
    tries = tries

    noEntries = noEntries

    satisfiedEntry = 0

    count = 0

    # under tries
    while count < tries:
        # empty array each iteration
        entriesResult = []

        k = 0

        # for each random entry we want to have sets of 7
        while k < noEntries:
            # fetching a random entry with the help of df.sample() which does that with the argument n that expresses the number of entries
            randomEntry = df.sample(n=noEntries)
            # if the random probability is equal or under 'probA' (the probability of event A occurring) 
            for i in range(noEntries):
                # we check for our event (the number of text reviews being less than 50)
                if randomEntry.text_reviews_count.iloc[i] < 50:
                    # we conclude event A occured and append it to the iteration array
                    entriesResult.append("A")
                else: 
                    # if not, we append "notA" simply to indicate when our event is not satisfied
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

print(simulateProbability(1000, 7))

## NOTE: As the number of tries increases, both code cells give the same result (or their difference is very small), but since excecution time for this one is higher, I decided to stick with 1000 tries for testing.

