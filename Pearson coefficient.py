#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The Pearson correlation coefficient (named for Karl Pearson) can be used to summarize the strength of the linear
#relationship between two data samples i.e how strong the two variables are correlated to each other.

#Pearson's correlation to help us understand the relationships between the feature values (independent values) 
#and the target value (dependent value or the value to be predicted ) 

#Pearson's correlation coefficient = covariance(X, Y) / (stdv(X) * stdv(Y))

#The use of mean and standard deviation in the calculation suggests the need for the two data samples to have a Gaussian 
#or Gaussian-like distribution.


#PEARSON CORRELATION COEFFICIENT is appropriate when X = quantitative and Y = quantitative

# Other situation , if your data has normal distribution and scale in this case you can use Pearson , 
#but if your data has not normal distributed you must use Spearman .

# coefficient returns a value between -1 and 1 that represents the limits of correlation.Where often a value below -0.5 or 
#above 0.5 indicates a notable correlation

#Q)what are the type of distribution?



# In[2]:


cd C:\Users\1185833\Downloads


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()

#histogram and normal probability plot
from scipy.stats import norm


# In[4]:


data=pd.read_csv('headbrain3.csv')
#check if the data has gaussian distribution


# In[5]:


#A normal Distribution is given if your data is symmetrical, bell-shaped, centered and unimodal.


#A normally distributed curve will have data  gathered around the mean and the  standard deviation will be  the measure
#of how spread out a normally distributed set of data is. 

#The steeper the bell curve, the smaller the standard deviation.If the data  are spread far apart, the bell curve 
#will be much flatter, meaning the standard deviation is large.

#https://www.varsitytutors.com/hotmath/hotmath_help/topics/normal-distribution-of-data


# In[6]:


# MAin point of normaly distributed graph is 


#a)Modality : The modality of a distribution is determined by the number of peaks it contains.
#-Unimodal means that there is only one peak.

#c)Skewness
#- Skewness is a measurement of the symmetry of a distribution.
# if the data is positively or negatively skewed

#c)Kurtosis
#-Kurtosis measures whether your dataset is heavy-tailed or light-tailed compared to a normal distribution.


# In[15]:


data


# In[7]:


sns.distplot(data['Brain Weight(grams)']);
#skewness and kurtosis
print("Skewness: %f" % data['Brain Weight(grams)'].skew())
print("Kurtosis: %f" % data['Brain Weight(grams)'].kurt())

#histogram and normal probability plot
from scipy.stats import norm

sns.distplot(data['Brain Weight(grams)'], fit=norm);
fig = plt.figure()
res = stats.probplot(data['Brain Weight(grams)'], plot=plt)

#Normal probability plot - Data distribution should closely follow the diagonal that represents the normal distribution


# In[10]:






w=data.iloc[:,0:1].values
y=data.iloc[:,1:2].values


# In[11]:


x=data.iloc[:,2:3].values
#this will create a variable y which has the target value i.e brain weight
z=data.iloc[:,3:4].values


# In[12]:


print(round(data['Gender'].corr(data['Brain Weight(grams)'])))          
plt.scatter(x,z,c='red')
plt.title('scattered graph for coorelation between Gender and brainweight' )
plt.xlabel('age')
plt.ylabel('brain weight')
plt.show()

#The Pearson corr coeficient value for variable gender and Brain weight is -0.0 i.e there is no relationship between the 
#two variable.
#Similarly graph below also tells the same that the two variable is nowhere correlated.


# In[13]:


print(round((data['Head Size(cm^3)'].corr(data['Brain Weight(grams)']))))         
plt.scatter(x,z,c='red')
plt.title('scattered graph for coorelation between head size and brainweight' )
plt.xlabel('head size')
plt.ylabel('brain weight')
plt.show()


# graph below signifies that there exists a perfect linear relationship between brain weight and head size 


# In[14]:


data.info()
data['Head Size(cm^3)'].corr(data['Brain Weight(grams)'])
k=data.corr()

print("The table for all possible values of pearson's coefficients is as follows")
print(k)

