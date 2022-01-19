#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np 
import pandas as pd


# In[21]:


tips = sns.load_dataset('tips')


# In[22]:


tips.head()


# In[23]:


sns.countplot(x = 'day' , data = tips) #this is to get the number of days in which smocking is highest in the dataset using count plot


# In[24]:


sns.countplot(x = 'smoker' , data = tips)


# In[25]:


sns.countplot(x = 'time' , data = tips)


# In[26]:


sns.pointplot(x = 'total_bill' , y = 'day' ,data = tips , color = 'green') #this is using the pointplot to get the plot using the available data


# In[27]:


sns.pointplot(x = 'day' , y = 'total_bill' ,data = tips , color = 'green') #this is using the pointplot to get the plot using the available data


# In[28]:


sns.factorplot(x = 'day' , y = 'total_bill' ,data = tips , color = 'green', kind="box") #this is using the factorplot to get the plot using the available data


# In[29]:


sns.catplot(x = 'day' , y = 'total_bill' ,data = tips , color = 'green') #this is using the catplot to get the plot using the available data


# In[30]:


sns.swarmplot(x = 'day' , y = 'total_bill' ,data = tips) #this is using the swarmplot to get the plot using the available datasets


# In[31]:


sns.swarmplot(x = 'day' , y = 'total_bill' ,data = tips, hue = 'sex') #this is using the swarmplot to get the plot using the available datasets


# In[32]:


sns.swarmplot(x = 'smoker' , y = 'tip' ,data = tips, hue = 'sex')


# In[33]:


sns.stripplot(x = 'smoker' , y = 'tip' ,data = tips, hue = 'sex') #this is using the stripplot to get the plot using the available datasets


# In[38]:


sns.barplot(x = 'day' , y = 'tip', data=tips, hue='sex')#this is using the barplot to get the plot using the available datasets


# In[36]:


sns.boxplot(x = 'day' , y = 'tip', data=tips)#this is using the boxplot to get the plot using the available datasets


# In[37]:


sns.boxplot(x = 'day' , y = 'tip', data=tips, hue = 'sex')#this is using the boxplot to get the plot using the available datasets


# In[40]:


sns.violinplot(x = 'day' , y = 'tip', data=tips, hue = 'sex', palete="cool")#this is using the violinplot to get the plot using the available datasets


# In[ ]:




