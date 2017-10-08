
# coding: utf-8

# In[40]:


import pandas as pd
import pickle
from nltk import word_tokenize as wt
from nltk import pos_tag as pt


# In[41]:


df = pd.read_csv('newcsvfile.txt', delimiter='\t')
temp = []


# In[42]:


for i in range(0,len(df),5):
    text = df.iloc[i][0] # i goes 0, 5, 10, 15, 20, 25 ...
    textTemp = pt(wt(text))
#     print textTemp
    finalArray = []
    for tags in textTemp:
        if 'VB' in tags[1]:
            print tags
            tags = list(tags)
            finalArray.append(tags[0] + ' not')
            tags = tuple(tags)
        else:
            finalArray.append(tags[0])
    newText = ' '.join(t for t in finalArray)
    temp.append([text, newText, [1,0]])
    print '{} ===> {}'.format(text, newText)


# In[43]:


len(temp)


# In[30]:


pt(wt('That\'s an average of 40,000 search queries every second'))


# In[44]:


df.head()


# In[46]:


randomLines = open('modiSpeech.txt', 'r').read().split('\n')
lalala = []
for lines in randomLines:
    lalala.extend(lines.split('.'))


# In[47]:


len(lalala)


# In[49]:


lalala = [i for i in lalala if len(i) > 40 and len(i) < 200]


# In[50]:


len(lalala)


# In[59]:


temp1 = []
import random


# In[60]:


random.randint(0,1598)


# In[61]:


passedNumbers = [99999]
for i in range(0,len(df),5):
    index = 99999
    while(index in passedNumbers):
        index = random.randint(0,1598)
    temp1.append([df.loc[i][0], lalala[index], [1,0]])
for i in range(0,len(df),5):
    index = 99999
    while(index in passedNumbers):
        index = random.randint(0,1598)
    temp1.append([df.loc[i][0], lalala[index], [1,0]])


# In[62]:


len(temp1)


# In[63]:


temp1[50]


# In[64]:


grandFinale = []
grandFinale.extend(temp1)


# In[65]:


len(grandFinale)


# In[66]:


grandFinale.extend(temp)


# In[67]:


len(grandFinale)


# In[68]:


BASE_URL = "https://api.cognitive.microsoft.com/bing/v7.0/search"
headers = {'Ocp-Apim-Subscription-Key': 'cd18b9463d45418fa44af0837b59cb51'}


# In[69]:


def search(text):
    response = requests.get(BASE_URL, params={'q': text}, headers=headers).json()
    result_list = response['webPages']['value']
    relevant_sentence_list = []

    # Fetch various opinions and results from the search
    for res in result_list:
        # Eliminate noise from sentence
        noiseless_snip = re.sub('[^A-Za-z0-9 ]+', '', res['snippet']).lower()
        relevant_sentence_list.append(noiseless_snip)
    return relevant_sentence_list


# In[77]:


from tqdm import tqdm
import requests, re
someArray = []
someBackupArray = []
for i in tqdm(range(0,len(df),5)):
    origtext = df.iloc[i][0]
    text = pt(wt(origtext))
    tempString = ''
    count = 0
    for tags in text:
        if 'NN' in tags[1]:
            tempString = tempString + ' ' + tags[0] + ' '
            count += 1
        if count == 3:
            break
    if count < 3:
        try:
            permstring = ' '.join(t for t in random.shuffle(origtext.split()))
        except:
            permstring = origtext[0:10]
        tempString = ' '.join(t for t in permstring.split()[:3])
    result = search(tempString)
    count = 0
    for res in result:
        if res not in someBackupArray:
            someBackupArray.append(res)
            someArray.append([origtext, res, [1,0]])
            count += 1
        if count == 2:
            break


# In[78]:


len(someArray)


# In[82]:


someArray[1]


# In[80]:


grandFinale.extend(someArray)


# In[81]:


len(grandFinale)


# In[83]:


pickle.dump(grandFinale, open('trainingnegative.p', 'w'))


# In[ ]:




