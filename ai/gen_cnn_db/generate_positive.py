
# coding: utf-8

# In[69]:


import pandas as pd
import pickle


# In[70]:


file = open('newcsvfile.csv', 'r')


# In[71]:


file = file.readlines()


# In[72]:


df = pd.read_csv('newcsvfile.txt', delimiter='\t')


# In[73]:


for i in file:
    i = i.split('",')
    if len(i) != 3:
        try:
            xyz = i[1].split(',')
            if len(xyz) == 2:
                i[0] = i[0].extend(xyz)
                temp.append(i[0])
            else:
                xyz = i[0].split(',')
                xyz = xyz.extend(i[1])
                temp.append(xyz)
        except:
            pass
    else:
        temp.append(i)
        


# In[74]:


df.tail()


# In[75]:


temp = []


# In[76]:


for i in range(len(df)):
    temp.append([df.iloc[i][0], df.iloc[i][1], [0,1]])


# In[77]:


len(temp)


# In[78]:


pickle.dump(temp, open('trainingpositive.p', 'w'))


# In[ ]:





# In[ ]:




