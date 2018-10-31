#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


help(json)


# In[5]:


Books={}
Books['gaurav']={
    'age':30,
    'gen':'male'
}

Books['henry']={
    'age':45,
    'gen':'male'
}


# In[6]:


json.dumps(Books)


# In[7]:


Books


# In[8]:


type(json.dumps(Books))


# In[9]:


##dumps converts it into a string 


# In[16]:


json_file = open("sData.json","r",encoding="utf-8")
cars = json.load(json_file)


# In[17]:


cars


# In[18]:


json_file.close()


# In[19]:


cars['buying']


# In[20]:


type(cars)


# In[21]:


json.dumps(cars)


# In[24]:


s=json.dumps(cars,ensure_ascii=False)


# In[25]:


#to save it to another file:


# In[26]:


file2=open("sDataCopy.txt","w",encoding="utf-8")


# In[27]:


json.dump(cars,file2,ensure_ascii=False)


# In[28]:


file2.close()


# In[34]:


f=open('sDataCopy.txt','r')


# In[30]:


f.readlines()


# In[33]:


f.close()


# In[ ]:




