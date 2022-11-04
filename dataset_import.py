#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# use this cell to import the data
import pandas as pd

# reading csv from url
df = pd.read_csv("https://docs.google.com/spreadsheets/d/1if5bG_Nld7iQC3FcUBIv2SLT12HQSCqvawvN67iZ-yE/gviz/tq?tqx=out:csv")
# df.head(10)

# getting entries for subgroups 
# getting entries for books longer than 500 pages
dataAboveThreshold = df[df['num_pages'] >= 500]
# dataAboveThreshold.head(10)

# getting entries for books shorter than 500 pages
dataUnderThreshold = df[df['num_pages'] < 500]
# dataUnderThreshold.head(10)

