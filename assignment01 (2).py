#!/usr/bin/env python
# coding: utf-8

# In[8]:


result = 0
for n in range(10, 100000):
    if n % 20 == 0: 
        result += 1
print(result)

