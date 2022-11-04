#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
dataAboveThreshold = df[df['num_pages'] >= 500]
dataUnderThreshold = df[df['num_pages'] < 500]

# created reasonable bins for a better observation of the histograms
bins = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5]

# the first graph
# average ratings with all books 
# df.average_rating, df.num_pages
# using numpy's np.array() to create an array and plot it in a histogram
averageRatingsAllData = np.array(df.average_rating)
plt.hist(averageRatingsAllData, bins, facecolor='r', alpha=0.7, edgecolor='k', linewidth=1)
plt.title("Average book ratings distribution from data of all books")
plt.xlabel("Average Rating")
plt.ylabel("Frequency")
# displaying all bins 
plt.xticks(bins[::1]) 
# rotating ticks as they would overlap
plt.xticks(rotation = 45)
plt.show()


# the second graph
# average ratings with books >= 500
# dataAboveThreshold.average_rating, dataAboveThreshold.num_pages
averageRatingsAboveThreshold = np.array(dataAboveThreshold.average_rating)
plt.hist(averageRatingsAboveThreshold, bins, facecolor='r', alpha=0.7, edgecolor='k', linewidth=1)
plt.title("Average book ratings distribution from data of books containing 500 or more pages")
plt.xlabel("Average Rating")
plt.ylabel("Frequency")
plt.xticks(bins[::1]) 
plt.xticks(rotation = 45)
plt.show()

# the third graph
# average ratings with with book < 500 pages 
# dataUnderThreshold.average_rating, dataUnderThreshold.num_pages
averageRatingsUnderThreshold = np.array(dataUnderThreshold.average_rating)
plt.hist(averageRatingsUnderThreshold, bins, facecolor='r', alpha=0.7, edgecolor='k', linewidth=1)
plt.title("Average book ratings distribution from data of books containing less than 500 pages")
plt.xlabel("Average Rating")
plt.ylabel("Frequency")
plt.xticks(bins[::1]) 
plt.xticks(rotation = 45)
plt.show()


# both subgroups graphs in the same axes 
# comparing them on relative frequencies, because comparing them on absolute frequencies wouldn't tell us anything meaningful, instead would probably yield misleading data
plt.hist(averageRatingsAboveThreshold, bins, facecolor='r', alpha=1, edgecolor='k', linewidth=1, weights=np.ones_like(averageRatingsAboveThreshold) / len(averageRatingsAboveThreshold), label="Books >= 500 pages")
plt.hist(averageRatingsUnderThreshold, bins, facecolor='b', alpha=.5, edgecolor='k', linewidth=1, weights=np.ones_like(averageRatingsUnderThreshold) / len(averageRatingsUnderThreshold), label="Books < 500 pages")
plt.xlabel("Average Rating")
plt.ylabel("Relative Frequency")
plt.legend()
plt.xticks(bins[::1]) 
plt.xticks(rotation = 45)
plt.show()

# plotting a scatterplot for the two variables to explain their correlation
plt.scatter(df.average_rating, df.num_pages, marker='.', linewidth=2)
plt.xlabel("Average Rating")
plt.ylabel("Book pages")
plt.xticks(rotation = 45)
plt.title("Average Ratings and Book Pages correlation")
plt.show()

