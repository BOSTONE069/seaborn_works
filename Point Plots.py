#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import numpy as np 
import pandas as pd


# In[3]:


diamond = sns.load_dataset('diamonds') # this is for loading data from the seaborn datasets


# In[5]:


print(diamond) #this is for printing the data sets


# In[6]:


print(diamond.head())#this is for checking if the data is successfully loaded


# In[13]:


sns.distplot(diamond['price']) # this is distribution plot from the data set


# In[10]:


sns.rugplot(diamond['x']) # this is the rug plot


# In[11]:


sns.rugplot(diamond['price']) # this is the rug plot


# In[12]:


sns.kdeplot(diamond['price']) # this is the kde plot


# In[14]:


sns.distplot(diamond['price'],kde=False) # this is distribution plot from the data set and removing kde plot


# In[ ]:




