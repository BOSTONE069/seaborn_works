#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np 
import pandas as pd


# In[6]:


dots = sns.load_dataset('dots') #thi is for loading the tips fron the seaborn data sets


# In[7]:


print(dots)


# In[8]:


dots.head() #this is for checking if the data is successfully loaded


# In[11]:


sns.pairplot(dots)


# In[12]:


sns.pairplot(dots , hue = 'choice') #hue command enales me to select the non numeric coulumn I would like to run in the dataset


# In[13]:


tips = sns.load_dataset('tips')


# In[15]:


print(tips)


# In[16]:


tips.head()


# In[17]:


sns.pairplot(tips)


# In[18]:


sns.pairplot(tips , hue = 'sex') #hue command enales me to select the non numeric coulumn I would like to run in the dataset


# In[19]:


sns.pairplot(tips , hue = 'day') #hue command enales me to select the non numeric coulumn I would like to run in the dataset


# In[20]:


sns.pairplot(tips , hue = 'smoker')


# In[24]:


x = sns.pairplot(tips , hue = 'day') #hue command enales me to select the non numeric coulumn I would like to run in the dataset
x.map_diag(sns.histplot) #this is for defining the type of graph you may want to use in the pair plots in the diagonal


# In[25]:


x = sns.pairplot(tips , hue = 'day') #hue command enales me to select the non numeric coulumn I would like to run in the dataset
x.map_diag(sns.distplot) #this is for defining the type of graph you may want to use in the pair plots in the diagonal


# In[29]:


x = sns.pairplot(tips , hue = 'day') #hue command enales me to select the non numeric coulumn I would like to run in the dataset
x.map_diag(sns.histplot) #this is for defining the type of graph you may want to use in the pair plots in the diagonal
x.map_upper(sns.kdeplot) #this is for defining the type of graph you may want to use in the pair plots in the for the upper part of the graph 
x.map_lower(sns.residplot)#this is for defining the type of graph you may want to use in the pair plots in the for the lower part of the graph


# In[ ]:




