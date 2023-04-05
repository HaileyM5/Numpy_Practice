#!/usr/bin/env python
# coding: utf-8

# # Numpy- inclass assignment 
# ## Submit your work using GitHub to Moodle

# ### Generate a random numpy array for Month of October where the highest temperature varies between 48-81 degree Farenheit
# - Keep in mind the length of the month
# - set a random seed of 1 for regenerate
# - Display the numpy array named `Temp_O` and find out the minimum and maximum temperature of month

# In[14]:


import numpy as np
np.random.seed(1)
Temp_O=np.random.randint(48,81,31)


# In[15]:


Temp_O


# In[ ]:





# ### Load the numpy file `Temp_December` and store it to a variable named Temp_D

# In[16]:


Temp_D=np.load('Temp_December.npy')


# In[17]:


Temp_D


# In[ ]:





# ### Compare two numpy array - Temp_O and Temp_D
# - Elementwise
# - Arraywise

# In[18]:


Temp_O>Temp_D


# In[19]:


Temp_O==Temp_D


# In[20]:


Temp_O<Temp_D


# ### Find out the:
# - Average temperature
# - Standard deviation
# - Varience
# - Minimum temp
# - Maximum temp
# - Median
# #### for Month of December

# In[21]:


print("Average Temp",Temp_D.mean())


# In[22]:


print("Standard deviation", round(Temp_D.std()))


# In[23]:


print("Min", Temp_D.mean())


# In[24]:


print("Max",Temp_D.max())


# In[52]:


print("Median",np.median(Temp_D))


# In[53]:


print("Variance",round(Temp_D.var()))


# In[ ]:





# ### Plot the distribution of December Temperature using Matplotlib
# - add title and create proper labels

# In[49]:


import matplotlib.pyplot as plt
plt.hist(Temp_D)


# In[ ]:





# ### Convert the Temp_D to Celsius and store it to a variable names Temp_C. 
# - Round off the result
# - Save it to a numpy file called DecemberTemp_Celsius

# In[32]:


Temp_D


# In[45]:


Temp_C=np.round((Temp_D-32)*5/9)


# In[46]:


Temp_C


# In[ ]:





# In[47]:


np.save("DecemberTemp_Celsius.npy", Temp_C)


# In[48]:


Y=np.load("DecemberTemp_Celsius.npy")
Y


# In[ ]:





# In[ ]:




