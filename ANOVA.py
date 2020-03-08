#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


data = pd.read_csv("scores.csv")
data.head(2)


# In[6]:


#Assumptions are

#The dependent variable i,e SAT scores should be continuous.
#The independent variables i.e districts should be two or more categorical groups(In this case we have 5 districts)
#There must be different participants in each group with no participant being in more than one group. In our case, each school cannot be in more than one district.
#The dependent variable should be approximately normally distributed for each category.
#Variances of each group are approximately equal.


# In[4]:


data['Borough'].value_counts()


# In[5]:


#There is no total score column, so we'll have to create it. In addition, we'll have to find the mean score of the each district across all schools.

data['total_score'] = data['Average Score (SAT Reading)'] +                        data['Average Score (SAT Math)']    +                        data['Average Score (SAT Writing)']
data = data[['Borough', 'total_score']].dropna()        
x = ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']
district_dict = {}

#Assigns each test score series to a dictionary key
for district in x:
    district_dict[district] = data[data['Borough'] == district]['total_score']


y = []
yerror = []
#Assigns the mean score and 95% confidence limit to each district
for district in x:
    y.append(district_dict[district].mean())
    yerror.append(1.96*district_dict[district].std()/np.sqrt(district_dict[district].shape[0]))    
    print(district + '_std : {}'.format(district_dict[district].std()))
    
sns.set(font_scale=1.8)
fig = plt.figure(figsize=(10,5))
ax = sns.barplot(x, y, yerr=yerror)
ax.set_ylabel('Average Total SAT Score')
plt.show()


# In[ ]:


#From our data exploration, we can see that the average SAT scores are quite different for each district. 
#We are interested in knowing if this is caused by random variation in data, or if there is an underlying cause.
#Since we have five different groups, we cannot use the t-test. Also note that the standard deviation of each group 
#are also very different, so we've violated one of our assumpions. However, we are going to use the 1-way ANOVA test 
#anyway just to understand the concepts.


# In[7]:


stats.f_oneway(
             district_dict['Brooklyn'], district_dict['Bronx'], \
             district_dict['Manhattan'], district_dict['Queens'], \
             district_dict['Staten Island']
)


# In[ ]:


# Looking into the lesser pvalue which is lesser that 0.05, we can say that we can readily reject the null hypothesis.


# In[8]:


districts = ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']

ss_b = 0
for d in districts:
    ss_b += district_dict[d].shape[0] *             np.sum((district_dict[d].mean() - data['total_score'].mean())**2)

ss_w = 0
for d in districts:
    ss_w += np.sum((district_dict[d] - district_dict[d].mean())**2)

msb = ss_b/4
msw = ss_w/(len(data)-5)
f=msb/msw
print('F_statistic: {}'.format(f))


# In[ ]:




