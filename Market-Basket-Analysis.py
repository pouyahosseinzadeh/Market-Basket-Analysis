
# coding: utf-8

# In[1]:


# Market-Basket-Analysis
# Pouya Hosseinzadeh

# for basic operations
import numpy as np
import pandas as pd

# for visualizations
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
from wordcloud import WordCloud
import networkx as nx

# for analysis
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder

# for defining path
import os


# In[2]:


# importing the two datasets and merging them based on the same column
df1 = pd.read_csv(r"D:\DRIVE D\daneshgah.arshad\UNISIENA\Advanced database systems(BigData)\DATASET/transactions.csv")
df2 = pd.read_csv(r"D:\DRIVE D\daneshgah.arshad\UNISIENA\Advanced database systems(BigData)\DATASET/segments-description.csv")
df = df1.merge(df2, on="COD_MKT_ID")


# In[3]:


# checking the head of the data
df.head()


# In[4]:


# checking the tail of the data
df.tail()


# In[5]:


# for simplicity we prefer to work on 10000 transactions rather than nearly 1 million which fails the computer RAM
df=df.iloc[0:10000]
df


# In[6]:


# making each transaction-id unique and create a new dataset that contains lists of items that are bought together
lst=[]
for item in df['SCONTRINO_ID'].unique():
    lst2=list(set(df[df['SCONTRINO_ID']==item]['SEGMENTO']))
    if len(lst2)>0:
        lst.append(lst2)
print(lst[0:3])
print(len(lst))


# In[7]:


# a good tool for data visualization to see the most popular items in SEGMENTO column
plt.rcParams['figure.figsize'] = (15, 15)
wordcloud = WordCloud(background_color = 'white', width = 1200,  height = 1200, max_words = 10000).generate(str(lst))
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Most Popular Items',fontsize = 20)
plt.show()


# In[8]:


# for Apriori algorithm, the dataset has to be one-hot encoded
te = TransactionEncoder()
te_lst = te.fit(lst).transform(lst)
data = pd.DataFrame(te_lst,columns=te.columns_)
data


# In[9]:


# Apriori Algorithm finds the frequent itemsets
frequent_items= apriori(data, use_colnames=True, min_support=0.03)
frequent_items.head()


# In[10]:


# Association rules function is used which can take any metric such as 'lift' and also the minimum threshold set to 1
rules = association_rules(frequent_items, metric="lift", min_threshold=1)
rules.antecedents = rules.antecedents.apply(lambda x: next(iter(x)))
rules.consequents = rules.consequents.apply(lambda x: next(iter(x)))
rules


# In[11]:


# a network graph to check association between antecedents and consequents
fig, ax=plt.subplots(figsize=(10,4))
GA=nx.from_pandas_edgelist(rules,source='antecedents',target='consequents')
nx.draw(GA,with_labels=True)
plt.show()

