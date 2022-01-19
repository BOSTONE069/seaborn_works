#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np 
import pandas as pd


# In[2]:


tips = sns.load_dataset('tips')


# In[3]:


flights = sns.load_dataset('flights')


# In[4]:


tips.head()


# In[5]:


flights.head()


# In[6]:


tip2 = tips.corr() #this enables the conversion of the values into matrix. It only pick the numerical colounms


# In[11]:


tip2


# In[7]:


flights2 = flights.corr()#this enables the conversion of the values into matrix. It only pick the numerical colounms


# In[12]:


flights2


# In[13]:


sns.heatmap(tip2, annot=True) #annot is for ensuring I have the values within the the boxes


# In[18]:


sns.heatmap(flights2, annot=True, linewidths=10, linecolor= 'blue')#the line with is for separation between the boxes while annot is for ensuring I have the values within the the boxes and c map is for changing the color of the graph


# In[19]:


sns.heatmap(flights2, annot=True, linewidths=10, linecolor= 'blue', cmap="cool")#the line with is for separation between the boxes while annot is for ensuring I have the values within the the boxes and c map is for changing the color of the graph


# In[20]:


flight3 = flights.pivot_table(index='month', columns="year", values="passengers") #the pivot helps in converting all the data in the table inform of matrix


# In[22]:


flight3


# In[26]:


sns.heatmap(flight3, annot=True, linewidths=2) #this is plotting using heatmap


# In[28]:


sns.clustermap(flight3, annot=True, linewidths=2, cmap='cool') #this is plotting using cluster map


# In[ ]:




