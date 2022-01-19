#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np 
import pandas as pd


# In[2]:


tips = sns.load_dataset('tips') #thi is for loading the tips fron the seaborn data sets


# In[4]:


print(tips)


# In[5]:


tips.head() #this is for checking if the data is successfully loaded


# In[6]:


sns.residplot(x='total_bill', y='tip' , data = tips) # this is for ploting a resid diagram


# In[7]:


sns.residplot(x='total_bill', y='tip' , data = tips , lowess=True) # this is for ploting a resid diagram and command lowess add a line to show the lower ditribution in the diagram


# In[8]:


sns.jointplot(x='total_bill', y='tip' , data = tips) # this is for ploting a joint diagram with scatter plot distribution as default


# In[10]:


sns.jointplot(x='total_bill', y='tip' , data = tips, kind='kde') #Kind enables you to define how the diagram is supposed to appear


# In[12]:


sns.jointplot(x='total_bill', y='tip' , data = tips, kind='hex', color = 'red') #Kind enables you to define how the diagram is supposed to appear


# In[13]:


sns.jointplot(x='total_bill', y='tip' , data = tips, kind='reg', color = 'green') #this is for plotting a regration plot defined by reg in the kind variable


# In[ ]:




