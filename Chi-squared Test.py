#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[6]:


df=pd.read_spss("colours.sav")


# In[7]:


df


# In[8]:


#To find if there is any correlatio between personality and colour preference

df=df.drop("case",axis=1)


# In[9]:


df.apply(lambda x: len(x.unique()))


# In[10]:


df.describe()


# In[11]:


#contigency table

contingency_table=pd.crosstab(df["person"],df["colour"])
print('contingency_table :-\n',contingency_table)


# In[12]:


Observed_Values = contingency_table.values 
print("Observed Values :-\n",Observed_Values)


# In[13]:


import scipy.stats
b=scipy.stats.chi2_contingency(contingency_table)


Expected_Values = b[3]
print("Expected Values :-\n",Expected_Values)


# In[16]:


#Degree of Freedom
no_of_rows=len(contingency_table.iloc[0:2,0])
no_of_columns=len(contingency_table.iloc[0,0:4])
df=(no_of_rows-1)*(no_of_columns-1)
print("Degree of Freedom:-",df)


# In[17]:


alpha=0.05


# In[19]:


from scipy.stats import chi2
chi_square=sum([(o-e)**2./e for o,e in zip(Observed_Values,Expected_Values)])
print(chi_square)
chi_square_statistic=chi_square[0]+chi_square[1]+chi_square[2]
print("chi-square statistic:-",chi_square_statistic)


# In[20]:


#critical_value
critical_value=chi2.ppf(q=1-alpha,df=df)
print('critical_value:',critical_value)


# In[25]:


#p-value
p_value=1-chi2.cdf(x=chi_square_statistic,df=df)
print('p-value:',p_value)


# In[29]:


print('Significance level: ',alpha)
print('Degree of Freedom: ',df)
print('chi-square statistic:',chi_square_statistic)
print('critical_value:',critical_value)
print('p-value:',p_value)


# In[27]:


if chi_square_statistic>=critical_value:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")
    
if p_value<=alpha:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")


# In[ ]:




