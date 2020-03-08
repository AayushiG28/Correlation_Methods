#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()

#histogram and normal probability plot
from scipy.stats import norm


# In[49]:


data_url = 'http://bit.ly/2cLzoxH'
# read data from url as pandas dataframe
df = pd.read_csv(data_url)
# let us select two relevant columns
df = df[['gdpPercap', 'lifeExp']]
print(df.head(3))


# In[50]:


sns.distplot(df['gdpPercap']);
#skewness and kurtosis
print("Skewness: %f" % df['gdpPercap'].skew())
print("Kurtosis: %f" % df['gdpPercap'].kurt())

#histogram and normal probability plot
from scipy.stats import norm

sns.distplot(df['gdpPercap'], fit=norm);
fig = plt.figure()
res = stats.probplot(df['gdpPercap'], plot=plt)

#Normal probability plot - Data distribution should closely follow the diagonal that represents the normal distribution

s


# In[51]:


#The above graph shows postively skewed data having kurtosis/tail and hence its is not normaly distributed around the mean


# In[61]:


#We will apply pearson coefficient and see what is the result 

pearson=np.corrcoef(gapminder.gdpPercap, gapminder.lifeExp)
spearman=gapminder.gdpPercap.corr(gapminder.lifeExp, method="spearman")

print("Pearson coefficient is :")
print(" ")
print(pearson)
print(" ")
print("Spearman coefficient is: ", spearman)


# In[ ]:


# we can see tha the major difference between spearman and pearson coefficient is that pearson coefficient assumes that the data is
#has normal distribution and when the assumption is not true, correlation value calculated in Pearson is reflecting only 
#the true association.

#Unlike Pearson coefficient, spearman doesn't assumes that there is a normal distributrrion and computes
#correlation coefficient on rank values of the data.


# In[ ]:




