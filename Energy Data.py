#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_excel("C:/Users/YBUCK MAX/Desktop/Python Project/Energy Data/Energy Data.xlsx")
df


# In[3]:


df.info()
df.shape


# In[4]:


df.isnull().sum()


# In[5]:


df.dropna(inplace=True)
df.info()


# In[19]:


#df.groupby("Year")["Energy Related CO2missions (Gigatonnes)"].mean()
#df.describe()
#mean_EnergyRelatedCO2missions = df.groupby("Year")["Energy Related CO2missions (Gigatonnes)"].mean().sort_values()
#mean_EnergyRelatedCO2missions
# CO2 emissions graph

plt.plot(df['Year'], df['Energy Related CO2missions (Gigatonnes)'],label='CO2 Emissions', linewidth=2, color='r')
plt.rcParams["figure.figsize"] = (8,16)
plt.xlabel('Year')
plt.ylabel('CO2 emissions in Gigatonnes')
plt.title('Emisssions trend in the last three decades')
plt.legend()
plt.grid()
plt.show()


# In[30]:


#How have global emissions of carbon dioxide (CO2) from fossil fuels and land use changed over time?
#create a figure plot with Four subplots and the production of Oil, Natural gas and Coal Trend over the decade (All four on same plot not subplots perse)
# plot lines
plt.plot(df['Year'], df['Energy Related CO2missions (Gigatonnes)'],label='CO2 Emissions', linewidth=2)
plt.plot(df['Year'], df['Oil Production (Million barrels per day)'],label='Oil Production', linewidth=2)
plt.plot(df['Year'], df['Natural Gas Production (Billion Cubic Metres)'],label='Natural Gas Production', linewidth=2)
plt.plot(df['Year'], df['Coal Production (million tons)'],label='Coal Production', linewidth=2)
plt.rcParams["figure.figsize"] = (8,16)
plt.xlabel('Year')
plt.ylabel('CO2 emissions in Gigatonnes')
plt.title('Emisssions trend in the last three decades')
plt.legend()
plt.grid()
plt.show()


# In[33]:


# Oil, Natural gas and Coal Production Trend

oil=df['Oil Production (Million barrels per day)']
N_gas=df['Natural Gas Production (Billion Cubic Metres)']
coal= df['Coal Production (million tons)']
emission = df['Energy Related CO2missions (Gigatonnes)']
y=df['Year']

# create a figure plot with three subplots

fig, (ax1, ax2, ax3, ax4)= plt.subplots(4,sharex=True, figsize=(20,16), constrained_layout=False)

#add title
ax1.set_title('Oil, Gas and Coal production over the last three decades')
#subplot for oil production
ax1.grid()
ax1.set_ylabel('Million barrels per day')
l1, = ax1.plot(y, oil, color='brown',lw=2,label='Oil Production')

#subplot for natural gas production
ax2.grid()
l2, = ax2.plot(y, N_gas, color='blue',lw=2,label='Natural Gas Production')
ax2.set_ylabel('Billion Cubic Metres')

# subplot for coal production
ax3.grid()
l3, = ax3.plot(y, coal, color='black',lw=2,label='Coal production')
ax3.set_ylabel('Million Tonnes')

# subplot for coal production
ax4.grid()
l4, = ax4.plot(y, emission, color='red',lw=2,label='C02 emission')
ax3.set_ylabel('Million Tonnes')

labels=['Oil Production','Natural Gas Production', 'Coal Production', 'C02 emission']
fig.tight_layout() 
fig.subplots_adjust(bottom=0.1)   ##  Need to play with this number.
fig.legend(labels=labels, loc="lower center", ncol=4)

plt.show()


# In[31]:


#create a figure plot with emissions from land use change subplots and the production 

#plt.plot(df['Year'], df['Energy Related CO2missions (Gigatonnes)'],label='CO2 Emissions', linewidth=2)
plt.plot(df['Year'], df['Hydroelectricity consumption in TWh'],label='Hydroelectricity consumption', linewidth=2)
plt.plot(df['Year'], df['Installed Solar Capacity (GW)'],label='Installed Solar Capacity', linewidth=2)
plt.plot(df['Year'], df['Installed Wind Capacity in GW'],label='Installed Wind Capacity', linewidth=2)
plt.rcParams["figure.figsize"] = (8,16)
plt.xlabel('Year')
plt.ylabel('CO2 emissions in Gigatonnes')
plt.title('Energy production and consumption trend in the last three decades')
plt.legend()
plt.grid()
plt.show()


# In[ ]:


# Electricity Generation

e=dataset['Electricity Generation (Terawatt-hours)']
h=dataset['Hydroelectricity consumption in TWh']
n= dataset['Nuclear energy consumption in TWh']
y=dataset['Year']

# create a figure plot with three subplots
fig, (ax1, ax2, ax3)= plt.subplots(3,sharex=True, figsize=(20,16), constrained_layout=False)


#add title
ax1.set_title('Global electricity generation Over the last 30 years')

#subplot for total electricity generated
ax1.grid()
ax1.set_ylabel('TWh')
l1, = ax1.plot(y, e, color='blue',lw=2)

#subplot for electricity generated from hydroelectiricy
ax2.grid()
l2, = ax2.plot(y, g, color='maroon',lw=2)
ax2.set_ylabel('TWh')

# subplot for electricity generated from nuclear energy
ax3.grid()
l3, = ax3.plot(y, g, color='black',lw=2)
ax3.set_ylabel('TWh')

labels=['Total Electricity Generation','Hydroelectricity', 'Nuclear Energy']
fig.tight_layout() 
fig.subplots_adjust(bottom=0.1)   ##  Need to play with this number.
fig.legend(labels=labels, loc="lower center", ncol=4)

plt.show()


# In[26]:


df.head()


# In[37]:


#create a stacked bar plot with Electricity consumption and generation over the decade 

#plt.plot(df['Year'], df['Energy Related CO2missions (Gigatonnes)'],label='CO2 Emissions', linewidth=2)
plt.bar(df['Year'], df['Electricity Generation (Terawatt-hours)'],label='Electricity Generation')
plt.bar(df['Year'], df['Hydroelectricity consumption in TWh'],label='Hydroelectricity consumption')
plt.xlabel('Year')
plt.ylabel('Electricity Generation and consumption rate(Terawatt-hours)')
plt.title('Energy production and consumption trend in the last three decades')
plt.legend()
plt.grid()
plt.show()



import numpy as np
 
#data
#x-axis
years = df['Year']
 
#bar chart properties
x = np.arange(len(years))
width = 0.3
 
#draw grouped bar chart
fig, ax = plt.subplots()
bar1 = ax.bar(x - width/2, df['Electricity Generation (Terawatt-hours)'], width, label='Electricity Generation')
bar2 = ax.bar(x + width/2, df['Hydroelectricity consumption in TWh'], width, label='Hydroelectricity consumption')
 
#
ax.set_xlabel('Year')
ax.set_ylabel('Electricity Generation and consumption rate(Terawatt-hours)')
ax.set_title('Energy production and consumption trend in the last three decades')
ax.set_xticks(x, years)
ax.legend()
 
#setting bar labels
ax.bar_label(bar1)
ax.bar_label(bar2)
 
fig.tight_layout()
plt.show()


# In[ ]:


# Compare Natural Energy (solar, water, wind) production and fossil (Oil, Natural gas and Coal)use 

