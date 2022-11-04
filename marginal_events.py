#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

# use this cell to determine the counts for the table below
n = len(df)
bookIDsAandB = []
# # # (A) Books whose number of text reviews is smaller than 50

textReviewsUnder50 = 0
for i in range(n):
    if df.text_reviews_count[i] < 50:
        textReviewsUnder50 += 1
        bookIDsAandB.append(df.bookID[i]) # check line 28 and below explanation

# # # (B) Books whose title starts with 'The'
allTitles = []
for i in range(n):
    allTitles.append(df.title[i])

TheCounter = 0
for i in range(n):
    titlesSplit = [*allTitles[i]]
    if titlesSplit[0] == "T" and titlesSplit[1] == "h" and titlesSplit[2] == "e" and titlesSplit[3] == " ": #making sure it's "The " not "The" because there is a book "Theories..."
        TheCounter += 1
        bookIDsAandB.append(df.bookID[i]) # check line 28 and below explanation

# # # Calculate A & B
# time to mess around :p
# while there are multiple ways to do this, I chose a fun one. I collected the bookIDs of the books that fulfilled the criteria for each event and pushed them into the same array
# then I looked up for duplicate IDs as that would mean that they appeared in both events, as that would mean that is a case where they happen both
# pd.Series() gets the array, and then returns boolean Series denoting duplicate rows by the values
# we are calculating the length of it to get the count of elements that are duplicate a.k.a appear in both A and B
AandB = len(pd.Series(bookIDsAandB)[pd.Series(bookIDsAandB).duplicated()].values)

print("How many As are there in the dataset? (Books text reviews < 50) -", textReviewsUnder50, "; The complement value of A? -", n - textReviewsUnder50, "; How many Bs are there in the dataset? (Book titles with 'The' -", TheCounter, "; The complement value of B? -", n - TheCounter, "; How many entries satisfy A and B? -", AandB)

