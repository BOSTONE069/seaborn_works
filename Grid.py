#!/usr/bin/env python
# coding: utf-8

# In[9]:


import seaborn as sns
import numpy as np 
import pandas as pd


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


tips = sns.load_dataset('tips')


# In[12]:


tips.head()


# In[15]:


sns.countplot(x ='smoker', data = tips)
sns.set_context('paper') #this is for styling the grid


# In[17]:


sns.countplot(x ='smoker', data = tips)
sns.despine() #this is for styling the grid by removing the borders


# In[19]:


sns.countplot(x ='smoker', data = tips)
sns.set_style('darkgrid') #this is for styling the background of the graph


# In[21]:


sns.countplot(x ='smoker', data = tips)
sns.set_style('whitegrid') #this is for styling the background of the graph


# In[ ]:




