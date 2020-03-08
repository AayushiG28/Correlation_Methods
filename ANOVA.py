#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


df = pd.read_csv("scores.csv")
df.head(2)


# In[31]:


#Assumptions are

#The dependent variable i,e SAT scores should be continuous.
#The independent variables i.e districts should be two or more categorical groups(In this case we have 5 districts)
#There must be different participants in each group with no participant being in more than one group. In our case, each school cannot be in more than one district.
#The dependent variable should be approximately normally distributed for each category.
#Variances of each group are approximately equal.


# In[32]:


df['Borough'].value_counts()


# In[33]:


df


# In[34]:


df['total_score'] = df['Average Score (SAT Reading)'] + df['Average Score (SAT Math)'] +df['Average Score (SAT Writing)']
df = df[['Borough', 'total_score']].dropna()        
col = ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']
district_dict = {}

#Assigns each test score series to a dictionary key
for district in col:
    district_dict[district] = data[data['Borough'] == district]['total_score']


y = []
y_1 = []
#Assigns the mean score and 95% confidence limit to each district
for district in col:
    y.append(district_dict[district].mean())
    y_1.append(1.96*district_dict[district].std()/np.sqrt(district_dict[district].shape[0]))    
    print(district + '_std : {}'.format(district_dict[district].std()))
    
sns.set(font_scale=1.8)
fig = plt.figure(figsize=(10,5))
ax = sns.barplot(x, y, yerr=y_1)
ax.set_ylabel('Average SAT Score')
plt.show()


# In[35]:


#From our data exploration, we can see that the average SAT scores are quite different for each district. 
#We are interested in knowing if this is caused by random variation in data, or if there is an underlying cause.
#Since we have five different groups, we cannot use the t-test. Also note that the standard deviation of each group 
#are also very different, so we've violated one of our assumpions. However, we are going to use the 1-way ANOVA test 
#anyway just to understand the concepts.


# In[36]:


stats.f_oneway(
             district_dict['Brooklyn'], district_dict['Bronx'], \
             district_dict['Manhattan'], district_dict['Queens'], \
             district_dict['Staten Island']
)


# In[37]:


# Looking into the lesser pvalue which is lesser that 0.05, we can say that we can readily reject the null hypothesis.


# In[39]:


districts = ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']


ss_b = 0
for d in districts:
    ss_b += district_dict[d].shape[0] *             np.sum((district_dict[d].mean() - data['total_score'].mean())**2)

ss_w = 0
for d in districts:
    ss_w += np.sum((district_dict[d] - district_dict[d].mean())**2)

#msb:estimated variance between groups 
#msw: estimated variance within groups

msb = ss_b/4
msw = ss_w/(len(data)-5)
f=msb/msw
print('F_statistic: {}'.format(f))


# In[ ]:




