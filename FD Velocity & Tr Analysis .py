#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_excel('fd vel chart.xlsx')


# In[3]:


data.count()


# In[4]:


data.Velocity.min(),data.Velocity.max()


# In[5]:


data.Tr.min(),data.Tr.max()


# In[7]:


data.plot(kind='scatter',x='Velocity',y='Tr')
plt.show()


# In[8]:


data.plot(kind='line',x='Velocity',y='Tr')
plt.show()


# In[ ]:




