#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Implementing Count Frequency Encoding
def count_frequency(data):
  
    # splitting sentences into words 
    data = data.split()         
    splits = []
    for i in data:             
        if i not in splits:
            splits.append(i) 
    words = [] 
    frequency = []
    for i in range(0, len(splits)):
        words.append(splits[i])
        
        frequency.append(splits.count(splits[i]))
        results = [words[i],frequency[i]]
    return results


# In[6]:


def save_in_list(results):
    a = []
    b = []
    for i in range(len(results)):
        a.append(results[i][0])
        b.append(results[i][1])
    return a,b


# In[8]:


# words=[]
# frequency=[]
import pandas as pd
def save_results(a,b):
    dictionary ={'words':a,'frequency':b}
    encoded_words = pd.DataFrame(dictionary)
    return encoded_words


# In[ ]:




