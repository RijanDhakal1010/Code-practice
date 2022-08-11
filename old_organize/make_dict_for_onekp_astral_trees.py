#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


df = pd.read_excel(".xlsx")


# In[ ]:


df.columns


# In[9]:


df2 = df.iloc[:,[1,2]]


# In[20]:


df2


# In[29]:


onekp_four_letter_code_to_species_name_dictv = dict()


# In[33]:


for i in df2.itertuples():
    key= i[1].rstrip()
    value = i[2].rstrip()
    onekp_four_letter_code_to_species_name_dictv[key] = value


# In[34]:


import pickle


# In[35]:


with open('onekp_name_codes.pickle', 'wb') as handle:
    pickle.dump(onekp_four_letter_code_to_species_name_dictv, handle, protocol=pickle.HIGHEST_PROTOCOL)

