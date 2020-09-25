#!/usr/bin/env python
# coding: utf-8

# # PROJECT

# # Creating an exploratory data analysis on TLC Trip Record Data

# I took 600 records of yellow taxi data in october 2019

# Importing Libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Importing data

# In[3]:


df = pd.read_csv('C:/Users/RAJAT SRIVASTAVA/Downloads/yellow_tripdata_2019-10.csv')
df


# In[4]:


df.head()


# Now, we dig in data to understand its various factors

# In[5]:


df.describe()


# We can clearly see that payment type, vendor id and passenger count are categorical data. Also, the amount can be negative. This indicates that due to some mistakes , there is a loss for taxi agency

# I ->We try to see whether fare amount and tip amount are in direct relation with trip distance

# In[6]:


x = df['fare_amount']
y = df['trip_distance']
x1 = df['tip_amount']
plt.xlabel("amount")
plt.ylabel("trip distance")
plt.scatter(x,y, label = 'fare amt', color = 'g')
plt.scatter(x1,y, label= 'tip amt', color = 'm')
plt.axhline(20)
plt.legend()
plt.title('Fig.1')
plt.show()


# We can see from the above graph that there is a direct coorelation between the fare amount and trip distance. Although there are a few exceptions like even though trip distance is zero , the person has payed . This maybe because the person has prebooked the ride and have not travelled in it. 
# The tip amount doesn't vary much with trip distance. A person often gives less tip as compared to the fare amount.

# II -> We now look does the more no. of passengers means more trip distance??

# In[7]:


x = df['passenger_count']
y = df['trip_distance']
plt.bar(x,y)
plt.xlabel('passenger count')
plt.ylabel('trip distance')
plt.title('fig 2')
plt.show()


# We observe that mostly a single passenger travels most distance . Also, higher no. of passenger travel less distance.

# III -> We now see which is the most common type of payment?

# In[8]:


df.groupby('payment_type')['VendorID'].count()


# It is clearly visible that 1 no. payment type is the most common.

# IV -> We see whether the extra charges are independent of the fare amount/trip distance with repect to vendorid.
# Also, we take into account each payment type to note differences.

# In[9]:


g= sns.relplot(x="fare_amount", y="extra", hue="VendorID", col="payment_type", data=df)


#  We obseve that the extra amount is either 0.5 or 3 and is independent of the fare amount. 

# ###### We also observe that vendor id 1 is payed more extra than vendor id 2.

# Payment 3 and 4 are mostly taken by vendor id 1.

# V -> We dig further and look whether pooling is beneficial?

# In[10]:


df['amtpperson'] = df['total_amount']/df['passenger_count']
df.head()


# Since trip distance is an important factor to be taken into account

# In[13]:


df['net'] = df['amtpperson']/df['trip_distance']
x= df['passenger_count']
y= df['net']
plt.xlabel('passenger count')
plt.ylabel('pooling amount')
plt.bar(x,y)
plt.show()


# Hence, we notice that pooling is not much beneficial.

# VI -> We look for the highest passenger count and its similarities

# In[14]:


df[df['passenger_count'] == df.passenger_count.max()]


# We clearly observe 
# 1. They travel mostly with vendor id 2
# 2. Rate code id used is 1.
# 3. Payment type is 1.

# #### THANK YOU

# #### SHRANKHLA SRIVASTAVA
# shrankhla.srivastava@gmail.com

# In[ ]:




